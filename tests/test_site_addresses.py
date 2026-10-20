"""SOT-87 (the owner, 2026-10-20: "make sure the docs site is available at docs.7110atc.com"): the site is served at
https://docs.7110atc.com/ and the product's hosts moved to 7110atc.com. No page, script or workflow may still point at the old
addresses. (AGENTS.md keeps them in its dated history entries, which is why it is not scanned.)
Run: python -m unittest discover -s tests -v"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OLD = re.compile(r"bandd\.cloud|xatc-7110\.github\.io")
# The README explains the custom domain, so it names the github.io host (the CNAME's target) on purpose.
README_OLD = re.compile(r"bandd\.cloud")


def sources():
    for root in ("docs", "scripts", ".github", "tests"):
        for path in (REPO / root).rglob("*"):
            if path.is_file() and path.suffix in {".md", ".yml", ".sh", ".py", ".css", ".svg"} and path != Path(__file__):
                yield path
    for name in ("mkdocs.yml", "README.md"):
        yield REPO / name


class AddressTests(unittest.TestCase):
    def test_site_url_is_the_custom_domain_at_its_root(self):
        text = (REPO / "mkdocs.yml").read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^site_url: https://docs\.7110atc\.com/$")

    def test_nothing_points_at_the_old_hosts(self):
        found = [f"{p.relative_to(REPO)}: {m.group(0)}" for p in sources()
                 for m in (README_OLD if p.name == "README.md" else OLD).finditer(p.read_text(encoding="utf-8"))]
        self.assertEqual(found, [])

    def test_the_pilot_site_is_app_7110atc_com(self):
        pages = "".join(p.read_text(encoding="utf-8") for p in (REPO / "docs").glob("*.md"))
        self.assertIn("https://app.7110atc.com/#/download", pages)
        self.assertIn("https://app.7110atc.com/#/privacy", pages)

    def test_the_move_notes_are_in_getting_started_and_troubleshooting(self):
        for name in ("getting-started.md", "troubleshooting.md"):
            text = (REPO / "docs" / name).read_text(encoding="utf-8")
            self.assertIn("0.20.0-rc.11", text, name)
            self.assertIn("app.7110atc.com/#/download", text, name)
            self.assertRegex(text, r"(?i)passkey", name)
            self.assertIn("2026-10-20", text, name)


if __name__ == "__main__":
    unittest.main()
