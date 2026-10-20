"""Tests of scripts/legacy_stubs.py on a sample tree. Run: python -m unittest discover -s tests -v"""
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import legacy_stubs  # noqa: E402

BASE = "https://docs.7110atc.com"
DOMAIN = "docs.7110atc.com"


def touch(root: Path, rel: str, text: str = "x") -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class StubTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.dest = Path(self._tmp.name) / "pages"
        # A deployed site: mike's root redirect, the manifest, a version and its alias, and the
        # old unversioned page that is still at the root.
        touch(self.dest, "index.html", "mike redirect")
        touch(self.dest, "versions.json", json.dumps([{"version": "1.0", "title": "1.0.0", "aliases": ["latest"]}]))
        for ver in ("1.0", "latest"):
            for page in ("", "getting-started/", "features/clearance/", "client/xplane-data/"):
                touch(self.dest, f"{ver}/{page}index.html", f"{ver} {page}")
            touch(self.dest, f"{ver}/assets/logo.svg")
            touch(self.dest, f"{ver}/search/search_index.json")
            touch(self.dest, f"{ver}/stylesheets/xatc.css")
            touch(self.dest, f"{ver}/404.html")
        touch(self.dest, "getting-started/index.html", "OLD getting started")
        # What the old unversioned build left at the root.
        touch(self.dest, "404.html", "OLD 404")
        touch(self.dest, "sitemap.xml")
        touch(self.dest, "sitemap.xml.gz")
        touch(self.dest, "search/search_index.json")
        touch(self.dest, "assets/logo.svg")
        touch(self.dest, "stylesheets/xatc.css")
        touch(self.dest, ".nojekyll", "")
        self.source = self.dest / "latest"
        touch(self.source, "404.html", "<!doctype html><html><head><title>NEW 404</title></head><body>NEW 404</body></html>")

    def run_stubs(self):
        return legacy_stubs.write_stubs(self.source, self.dest, BASE)

    def test_every_page_gets_a_stub_at_its_old_path(self):
        written = self.run_stubs()
        self.assertEqual(
            sorted(written),
            ["client/xplane-data/index.html", "features/clearance/index.html", "getting-started/index.html"],
        )
        for rel in written:
            self.assertTrue((self.dest / rel).is_file(), rel)

    def test_stub_redirects_to_latest_keeping_query_and_anchor(self):
        self.run_stubs()
        text = (self.dest / "features/clearance/index.html").read_text(encoding="utf-8")
        target = f"{BASE}/latest/features/clearance/"
        self.assertIn(f'<link rel="canonical" href="{target}">', text)
        self.assertIn(f'<meta http-equiv="refresh" content="0; url={target}">', text)
        self.assertIn(f'location.replace("{target}" + location.search + location.hash)', text)
        self.assertIn(f'<a href="{target}">', text)

    def test_the_old_page_is_replaced(self):
        self.run_stubs()
        text = (self.dest / "getting-started/index.html").read_text(encoding="utf-8")
        self.assertNotIn("OLD", text)
        self.assertIn(f"{BASE}/latest/getting-started/", text)

    def test_versions_manifest_and_root_redirect_are_untouched(self):
        before = {
            p.relative_to(self.dest).as_posix(): p.read_text(encoding="utf-8")
            for p in self.dest.rglob("*")
            if p.is_file() and p.relative_to(self.dest).parts[0] in ("1.0", "latest", "index.html", "versions.json")
        }
        self.run_stubs()
        after = {
            p.relative_to(self.dest).as_posix(): p.read_text(encoding="utf-8")
            for p in self.dest.rglob("*")
            if p.is_file() and p.relative_to(self.dest).parts[0] in ("1.0", "latest", "index.html", "versions.json")
        }
        self.assertEqual(before, after)

    def test_assets_search_and_404_are_not_pages(self):
        written = self.run_stubs()
        self.assertFalse(any(w.startswith(("assets", "search", "stylesheets", "404")) for w in written))

    def test_main_publishes_the_404_and_removes_the_old_build(self):
        rc = legacy_stubs.main(["--source", str(self.source), "--dest", str(self.dest), "--base-url", BASE])
        self.assertEqual(rc, 0)
        text = (self.dest / "404.html").read_text(encoding="utf-8")
        self.assertIn("NEW 404", text)
        self.assertNotIn("OLD 404", text)
        for gone in ("sitemap.xml", "sitemap.xml.gz", "search", "assets", "stylesheets"):
            self.assertFalse((self.dest / gone).exists(), gone)
        self.assertTrue((self.dest / ".nojekyll").exists())

    def test_the_root_404_sends_an_old_docs_prefix_address_to_the_root(self):
        # the old github.io project path (/docs/...): GitHub drops the prefix itself when it redirects to the custom
        # domain, and this is the second line of defence if a /docs/... address ever arrives here.
        legacy_stubs.publish_404(self.source, self.dest)
        text = (self.dest / "404.html").read_text(encoding="utf-8")
        self.assertIn('<head><script>if (location.pathname.indexOf("/docs/") === 0)', text)
        self.assertIn("location.replace(location.pathname.slice(5) + location.search + location.hash)", text)
        self.assertEqual(text.count("indexOf"), 1)
        # the same script, run on a path, yields the root path ("/docs/latest/privacy/" -> "/latest/privacy/")
        self.assertEqual("/docs/latest/privacy/"[5:], "/latest/privacy/")
        self.assertEqual("/docs/"[5:], "/")
        # the page without a <head> still gets it
        (self.source / "404.html").write_text("bare", encoding="utf-8")
        legacy_stubs.publish_404(self.source, self.dest)
        self.assertTrue((self.dest / "404.html").read_text(encoding="utf-8").startswith('<script>'))

    def test_cname_is_written_when_missing_and_replaced_when_wrong_and_left_alone_when_right(self):
        self.assertFalse((self.dest / "CNAME").exists())
        self.assertTrue(legacy_stubs.ensure_cname(self.dest, DOMAIN))
        self.assertEqual((self.dest / "CNAME").read_text(encoding="utf-8"), DOMAIN + "\n")
        self.assertFalse(legacy_stubs.ensure_cname(self.dest, DOMAIN))
        (self.dest / "CNAME").write_text("other.example.com\n", encoding="utf-8")
        self.assertTrue(legacy_stubs.ensure_cname(self.dest, DOMAIN))
        self.assertEqual((self.dest / "CNAME").read_text(encoding="utf-8"), DOMAIN + "\n")
        # the way GitHub writes it: no trailing newline is the same domain
        (self.dest / "CNAME").write_text(DOMAIN, encoding="utf-8")
        self.assertFalse(legacy_stubs.ensure_cname(self.dest, DOMAIN))

    def test_main_with_cname_writes_it(self):
        rc = legacy_stubs.main(["--source", str(self.source), "--dest", str(self.dest), "--base-url", BASE, "--cname", DOMAIN])
        self.assertEqual(rc, 0)
        self.assertEqual((self.dest / "CNAME").read_text(encoding="utf-8").strip(), DOMAIN)

    def test_main_without_cname_leaves_an_existing_one(self):
        touch(self.dest, "CNAME", DOMAIN + "\n")
        rc = legacy_stubs.main(["--source", str(self.source), "--dest", str(self.dest), "--base-url", BASE])
        self.assertEqual(rc, 0)
        self.assertEqual((self.dest / "CNAME").read_text(encoding="utf-8"), DOMAIN + "\n")

    def test_removing_the_old_build_leaves_versions_manifest_and_redirect(self):
        before = {
            p.relative_to(self.dest).as_posix(): p.read_text(encoding="utf-8")
            for p in self.dest.rglob("*")
            if p.is_file() and p.relative_to(self.dest).parts[0] in ("1.0", "latest", "index.html", "versions.json")
        }
        legacy_stubs.remove_stale_build(self.dest)
        legacy_stubs.publish_404(self.source, self.dest)
        after = {
            p.relative_to(self.dest).as_posix(): p.read_text(encoding="utf-8")
            for p in self.dest.rglob("*")
            if p.is_file() and p.relative_to(self.dest).parts[0] in ("1.0", "latest", "index.html", "versions.json")
        }
        self.assertEqual(before, after)

    def test_removing_twice_is_fine(self):
        self.assertEqual(
            sorted(legacy_stubs.remove_stale_build(self.dest)),
            ["assets", "search", "sitemap.xml", "sitemap.xml.gz", "stylesheets"],
        )
        self.assertEqual(legacy_stubs.remove_stale_build(self.dest), [])

    def test_main_without_a_404_in_the_source_deletes_nothing(self):
        (self.source / "404.html").unlink()
        rc = legacy_stubs.main(["--source", str(self.source), "--dest", str(self.dest), "--base-url", BASE])
        self.assertEqual(rc, 1)
        self.assertTrue((self.dest / "assets/logo.svg").is_file())
        self.assertEqual((self.dest / "404.html").read_text(encoding="utf-8"), "OLD 404")

    def test_a_version_folder_named_like_an_old_file_is_never_deleted(self):
        touch(self.dest, "versions.json", json.dumps([{"version": "search", "title": "x", "aliases": []}]))
        with self.assertRaises(SystemExit):
            legacy_stubs.remove_stale_build(self.dest)

    def test_running_twice_gives_the_same_files(self):
        first = self.run_stubs()
        text = (self.dest / "features/clearance/index.html").read_text(encoding="utf-8")
        self.assertEqual(first, self.run_stubs())
        self.assertEqual(text, (self.dest / "features/clearance/index.html").read_text(encoding="utf-8"))

    def test_a_page_named_like_a_version_is_refused(self):
        touch(self.source, "1.0/index.html")
        with self.assertRaises(SystemExit):
            self.run_stubs()

    def test_main_fails_when_the_source_has_no_pages(self):
        empty = Path(self._tmp.name) / "empty"
        empty.mkdir()
        rc = legacy_stubs.main(["--source", str(empty), "--dest", str(self.dest), "--base-url", BASE])
        self.assertEqual(rc, 1)

    def test_every_deep_link_known_to_other_repositories_has_a_stub(self):
        # The pages the client, the pilot site and the docs themselves link to (docs/getting-started/,
        # docs/privacy/, and the site root).
        self.run_stubs()
        touch(self.source, "privacy/index.html")
        legacy_stubs.write_stubs(self.source, self.dest, BASE)
        for page in ("getting-started", "privacy"):
            text = (self.dest / page / "index.html").read_text(encoding="utf-8")
            self.assertTrue(re.search(rf'url={re.escape(BASE)}/latest/{page}/"', text), page)


if __name__ == "__main__":
    unittest.main()
