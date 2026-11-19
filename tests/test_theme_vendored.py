"""The shared theme is a pinned copy (SOT-260; the plan's section 3: ``theme.lock``, ``scripts/sync_theme.sh``, a manifest test).
``docs/assets/theme/`` holds the brand repo's release exactly: every file matches the theme's own MANIFEST.json, the manifest's
version is the lock's and nothing else sits in the folder. A hand edit, an extra file or a missing one fails here: change the theme
upstream and run ``scripts/sync_theme.sh <version>``. The contrast tests check the pairs docs/stylesheets/xatc.css draws from the
theme's raw palette, in both schemes (text 4.5:1, non-text 3:1).
Run: python -m unittest discover -s tests -v"""
import hashlib
import json
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
THEME = REPO / "docs" / "assets" / "theme"
LOCK = REPO / "theme.lock"


def manifest():
    return json.loads((THEME / "MANIFEST.json").read_text(encoding="utf-8"))


def palette():
    css = (THEME / "tokens.css").read_text(encoding="utf-8")
    return dict(re.findall(r"--s71-([a-z-]+):\s*(#[0-9A-Fa-f]{6});", css))


def luminance(hex_):
    ch = [int(hex_[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    ch = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in ch]
    return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]


def contrast(a, b):
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


class ThemeVendoredTests(unittest.TestCase):
    def test_the_lock_names_a_version_and_a_sha256(self):
        lock = json.loads(LOCK.read_text(encoding="utf-8"))
        self.assertEqual(set(lock), {"version", "sha256"})
        self.assertRegex(lock["version"], r"^\d+\.\d+\.\d+$")
        self.assertRegex(lock["sha256"], r"^[0-9a-f]{64}$")

    def test_the_copy_is_the_locked_version(self):
        lock = json.loads(LOCK.read_text(encoding="utf-8"))
        self.assertEqual(manifest()["name"], "seventyoneten-theme")
        self.assertEqual(manifest()["version"], lock["version"])

    def test_every_file_matches_the_manifest_and_none_is_extra(self):
        m = manifest()
        on_disk = {p.relative_to(THEME).as_posix() for p in THEME.rglob("*") if p.is_file()} - {"MANIFEST.json"}
        self.assertEqual(on_disk, set(m["files"]), "files added or missing: run scripts/sync_theme.sh")
        edited = [n for n, d in m["files"].items() if hashlib.sha256((THEME / n).read_bytes()).hexdigest() != d]
        self.assertEqual(edited, [], "edited by hand (change the theme upstream)")

    def test_the_build_links_the_theme_files_and_the_fonts_exist(self):
        yml = (REPO / "mkdocs.yml").read_text(encoding="utf-8")
        order = [yml.index(f"  - {name}") for name in ("assets/theme/tokens.css", "assets/theme/fonts.css",
                                                         "assets/theme/shape-soft.css", "stylesheets/xatc.css")]
        self.assertEqual(order, sorted(order), "tokens, fonts, shape, then the site's own css")
        self.assertNotIn("fonts.googleapis", yml)
        self.assertNotIn("shape-room", yml)
        fonts = (THEME / "fonts.css").read_text(encoding="utf-8")
        for url in re.findall(r'url\("([^"]+)"\)', fonts):
            self.assertTrue((THEME / url).is_file(), url)

    def test_the_stylesheet_has_no_literal_colours(self):
        css = (REPO / "docs" / "stylesheets" / "xatc.css").read_text(encoding="utf-8")
        css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
        self.assertEqual(re.findall(r"#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(", css), [])


class ContrastTests(unittest.TestCase):
    """(foreground, background, minimum) as the stylesheet pairs them, per scheme."""

    SCHEMES = {
        "night": dict(bg="night", panel="panel", deep="deep-night", text="paper", dim="dim", accent="teal", warn="warn",
                      warn_bg="warn-bg-night", tx="red-text", ok_bg="ok-bg-night", err_bg="err-bg", line="line-night",
                      on_accent="night"),
        "paper": dict(bg="paper", panel="paper-card", deep="deep-light", text="night", dim="dim-light", accent="teal-deep",
                      warn="warn-light", warn_bg="warn-bg-light", tx="red-text-light", ok_bg="ok-bg-light", err_bg="err-bg-light",
                      line="line-light", on_accent="paper"),
    }

    def test_text_pairs(self):
        p = palette()
        for name, s in self.SCHEMES.items():
            pairs = [("text", "bg"), ("text", "panel"), ("text", "deep"), ("dim", "bg"), ("dim", "panel"), ("dim", "deep"),
                     ("accent", "bg"), ("accent", "panel"), ("accent", "deep"), ("warn", "warn_bg"), ("text", "warn_bg"),
                     ("text", "ok_bg"), ("tx", "err_bg"), ("on_accent", "accent")]
            for fg, bg in pairs:
                ratio = contrast(p[s[fg]], p[s[bg]])
                self.assertGreaterEqual(ratio, 4.5, f"{name}: {fg} on {bg} is {ratio:.2f}:1")

    def test_paper_search_placeholder_and_kicker(self):
        p = palette()
        # the open search field is paper below 60em: its placeholder is --s71-dim-light there (it was --s71-dim, 2:1)
        self.assertGreaterEqual(contrast(p["dim-light"], p["paper"]), 4.5)
        # the hero kicker in paper: --s71-teal-hover-light on the hero panel under a 25% teal-deep tint (the 12% tint plus the 16% glow, worst case)
        card, deep = p["paper-card"], p["teal-deep"]
        mixed = "#" + "".join(f"{round(int(card[i:i + 2], 16) * 0.75 + int(deep[i:i + 2], 16) * 0.25):02X}" for i in (1, 3, 5))
        self.assertGreaterEqual(contrast(p["teal-hover-light"], mixed), 4.5)

    def test_chrome_pairs(self):
        p = palette()
        for fg, bg in (("paper", "panel"), ("dim", "panel"), ("teal", "panel"), ("paper", "deep-night"), ("dim", "deep-night")):
            self.assertGreaterEqual(contrast(p[fg], p[bg]), 4.5, f"chrome: {fg} on {bg}")

    def test_non_text_pairs(self):
        p = palette()
        for name, s in self.SCHEMES.items():
            # the focus and accent marks (a tab's underline, a card's hover ring) against the page
            self.assertGreaterEqual(contrast(p[s["accent"]], p[s["bg"]]), 3.0, name)


if __name__ == "__main__":
    unittest.main()
