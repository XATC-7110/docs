"""scripts/deploy-versioned.sh run for real against a throwaway repository and a bare 'origin', with stand-ins
for mkdocs and mike (the real ones are not needed: what is tested is what the script adds to the gh-pages root).

SOT-87: the site is served at docs.7110atc.com, so GitHub Pages needs a CNAME file at the root of gh-pages, and the old
page addresses redirect to https://docs.7110atc.com/latest/<page>/.
Run: python -m unittest discover -s tests -v"""
import os
import shutil
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOMAIN = "docs.7110atc.com"

MKDOCS = """#!/usr/bin/env bash
# stand-in: mkdocs build --strict -d DIR
while [[ $# -gt 0 ]]; do if [[ "$1" == "-d" ]]; then mkdir -p "$2"; fi; shift; done
"""

# stand-in for `mike deploy --branch B ... VERSION [ALIAS]` and `mike set-default`: commits a built site into the
# local gh-pages branch, replacing only the version folder (and the alias) and leaving everything else as it is, which
# is what mike does.
MIKE = """#!/usr/bin/env python3
import os, shutil, subprocess, sys, tempfile
args = sys.argv[1:]
if args[0] != "deploy":
    sys.exit(0)
branch = args[args.index("--branch") + 1]
names = [a for a in args[1:] if a[0].isdigit() or a == "latest"]
version, aliases = names[0], names[1:]
repo = os.getcwd()
work = tempfile.mkdtemp()
def git(*a, cwd=work):
    subprocess.run(["git", "-c", "user.name=mike", "-c", "user.email=m@e.com", *a], cwd=cwd, check=True, capture_output=True)
has = subprocess.run(["git", "rev-parse", "--verify", "-q", "refs/heads/" + branch], cwd=repo, capture_output=True).returncode == 0
if has:
    git("clone", "--quiet", "--branch", branch, repo, work + "/w", cwd=repo)
else:
    os.makedirs(work + "/w"); git("init", "-q", "-b", branch, cwd=work + "/w")
site = work + "/w"
for name in [version, *aliases]:
    shutil.rmtree(site + "/" + name, ignore_errors=True)
    os.makedirs(site + "/" + name + "/getting-started")
    for rel, text in (("index.html", "home"), ("getting-started/index.html", "gs"), ("404.html", "<html><head><title>404</title></head></html>")):
        open(site + "/" + name + "/" + rel, "w").write(text)
open(site + "/index.html", "w").write("redirect")
open(site + "/versions.json", "w").write('[{"version": "%s", "title": "x", "aliases": %s}]' % (version, str(aliases).replace("'", '"')))
git("add", "-A", cwd=site); git("commit", "-q", "--allow-empty", "-m", "mike", cwd=site)
git("push", "-q", repo, "HEAD:refs/heads/" + branch, cwd=site)
"""


def run(cmd, cwd, env=None, check=True):
    return subprocess.run(cmd, cwd=cwd, env=env, check=check, capture_output=True, text=True)


class DeployScriptTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.origin = self.tmp / "origin.git"
        run(["git", "init", "-q", "--bare", str(self.origin)], self.tmp)
        self.work = self.tmp / "work"
        self.work.mkdir()
        (self.work / "scripts").mkdir()
        for name in ("deploy-versioned.sh", "legacy_stubs.py"):
            shutil.copy(REPO / "scripts" / name, self.work / "scripts" / name)
        self.bin = self.tmp / "bin"
        self.bin.mkdir()
        for name, body in (("mkdocs", MKDOCS), ("mike", MIKE)):
            path = self.bin / name
            path.write_text(body)
            path.chmod(path.stat().st_mode | stat.S_IEXEC)
        self.env = {**os.environ, "PATH": f"{self.bin}{os.pathsep}{os.environ['PATH']}",
                    "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@e.com",
                    "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@e.com"}
        self.env.pop("SITE_BASE_URL", None)
        self.env.pop("SITE_DOMAIN", None)
        run(["git", "init", "-q", "-b", "main"], self.work, self.env)
        run(["git", "remote", "add", "origin", str(self.origin)], self.work, self.env)
        (self.work / "README").write_text("x")
        run(["git", "add", "-A"], self.work, self.env)
        run(["git", "commit", "-q", "-m", "init"], self.work, self.env)
        run(["git", "push", "-q", "origin", "main"], self.work, self.env)

    def deploy(self, tag):
        run(["git", "tag", tag], self.work, self.env)
        run(["git", "push", "-q", "origin", tag], self.work, self.env)
        return run(["bash", "scripts/deploy-versioned.sh", tag], self.work, self.env)

    def pages(self) -> Path:
        out = self.tmp / f"pages-{len(list(self.tmp.glob('pages-*')))}"
        run(["git", "clone", "-q", "--branch", "gh-pages", str(self.origin), str(out)], self.tmp, self.env)
        return out

    def test_the_first_deploy_puts_the_cname_and_the_root_redirects_on_the_custom_domain(self):
        self.deploy("v1.0.0")
        pages = self.pages()
        self.assertEqual((pages / "CNAME").read_text().strip(), DOMAIN)
        stub = (pages / "getting-started" / "index.html").read_text()
        self.assertIn(f'url=https://{DOMAIN}/latest/getting-started/"', stub)
        self.assertNotIn("github.io", stub)
        self.assertNotIn("/docs/latest", stub)
        self.assertIn('indexOf("/docs/")', (pages / "404.html").read_text())

    def test_a_cname_that_went_missing_is_put_back_by_the_next_deploy(self):
        self.deploy("v1.0.0")
        pages = self.pages()
        run(["git", "rm", "-q", "CNAME"], pages, self.env)
        run(["git", "commit", "-q", "-m", "drop CNAME"], pages, self.env)
        run(["git", "push", "-q", "origin", "gh-pages"], pages, self.env)
        run(["git", "fetch", "-q", "origin", "gh-pages:gh-pages", "-f"], self.work, self.env)
        done = self.deploy("v1.0.1")
        self.assertIn("wrote CNAME", done.stdout)
        self.assertEqual((self.pages() / "CNAME").read_text().strip(), DOMAIN)

    def test_a_cname_github_wrote_without_a_newline_is_left_alone(self):
        self.deploy("v1.0.0")
        pages = self.pages()
        (pages / "CNAME").write_text(DOMAIN)
        run(["git", "commit", "-q", "-am", "GitHub's CNAME"], pages, self.env)
        run(["git", "push", "-q", "origin", "gh-pages"], pages, self.env)
        run(["git", "fetch", "-q", "origin", "gh-pages:gh-pages", "-f"], self.work, self.env)
        done = self.deploy("v1.0.1")
        self.assertNotIn("wrote CNAME", done.stdout)
        self.assertEqual((self.pages() / "CNAME").read_text(), DOMAIN)

    def test_site_domain_overrides_the_default(self):
        self.env["SITE_DOMAIN"] = "docs.example.test"
        self.deploy("v1.0.0")
        pages = self.pages()
        self.assertEqual((pages / "CNAME").read_text().strip(), "docs.example.test")
        self.assertIn("https://docs.example.test/latest/getting-started/", (pages / "getting-started" / "index.html").read_text())


if __name__ == "__main__":
    unittest.main()
