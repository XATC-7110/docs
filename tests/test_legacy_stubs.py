"""Tests of scripts/legacy_stubs.py on a sample tree. Run: python -m unittest discover -s tests -v"""
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import legacy_stubs  # noqa: E402

BASE = "https://xatc-7110.github.io/docs"


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
        self.source = self.dest / "latest"

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
        self.assertFalse((self.dest / "assets").exists())

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
