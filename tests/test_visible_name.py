"""SOT-119 (the owner, 2026-10-21: "It should be \"SeventyOneTen\"" and "xatc should not be anywhere"): no text a reader can
see says "xatc". The one exception is the installed app and its files, which are still named xatc-agent on disk until a client
change renames them; they stay literal where a page tells the reader what to click or type (ALLOWED below).
Not scanned: URLs and repository names are not in the pages, AGENTS.md and README.md are developer docs, the stylesheet's
file name and the comments in mkdocs.yml and the CSS are code.
Run: python -m unittest discover -s tests -v"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Literal names, exactly as they are on disk or as the client shows them today.
ALLOWED = [
    "xatc-agent-setup-<version>.exe",           # the Windows installer
    "xatc-agent-<version>-x86_64.AppImage",     # the Linux AppImage
    "xatc-agent-client",                        # the settings folder, the log file, the credential name
    "**xatc-agent client**",                    # the window's title
    "**xatc-agent**",                           # the app in the Start menu, Applications, the header, the AppImage window
    "Apps > xatc-agent >",                      # Windows Settings > Apps
    "This is xatc-agent 0.19.0,",               # the client's own banner, quoted
    '"xatc-agent is already running"',          # the client's own message, quoted
    "in the xatc-agent window first",           # the client's own reason, quoted
]


def visible_sources():
    for path in sorted((REPO / "docs").rglob("*")):
        if path.is_file() and path.suffix in {".md", ".svg"}:
            yield path, path.read_text(encoding="utf-8")
    text = (REPO / "mkdocs.yml").read_text(encoding="utf-8")
    # comments and the stylesheet's file name are code, not text
    text = "\n".join(l for l in text.split("\n") if not l.lstrip().startswith("#"))
    yield REPO / "mkdocs.yml", text.replace("stylesheets/xatc.css", "")


def strip_allowed(text):
    for literal in ALLOWED:
        text = text.replace(literal, "")
    return text


class VisibleNameTests(unittest.TestCase):
    def test_no_visible_text_says_xatc(self):
        found = []
        for path, text in visible_sources():
            for n, line in enumerate(strip_allowed(text).split("\n"), 1):
                if re.search(r"xatc", line, re.I):
                    found.append(f"{path.relative_to(REPO)}:{n}: {line.strip()[:100]}")
        self.assertEqual(found, [])

    def test_the_site_and_the_logo_are_named_seventyoneten(self):
        self.assertRegex((REPO / "mkdocs.yml").read_text(encoding="utf-8"), r"(?m)^site_name: SeventyOneTen$")
        self.assertIn('aria-label="SeventyOneTen"', (REPO / "docs/assets/logo.svg").read_text(encoding="utf-8"))

    def test_the_name_is_written_as_one_word_with_three_capitals(self):
        wrong = []
        for path, text in visible_sources():
            for m in re.finditer(r"seventy[\s-]?one[\s-]?ten|seventyoneten", text, re.I):
                if m.group(0) != "SeventyOneTen":
                    wrong.append(f"{path.relative_to(REPO)}: {m.group(0)}")
        self.assertEqual(wrong, [])

    def test_the_recording_question_says_seventyoneten_in_both_pages(self):
        quoted = []
        for name in ("getting-started.md", "privacy.md"):
            text = (REPO / "docs" / name).read_text(encoding="utf-8")
            m = re.search(r"(?m)^> \*\*Keep your radio audio to improve SeventyOneTen\?\*\* .*$", text)
            self.assertIsNotNone(m, name)
            quoted.append(m.group(0))
            self.assertIn("SeventyOneTen also keeps the text its speech recognizer wrote down", m.group(0), name)
            self.assertTrue(m.group(0).endswith(
                "Your flight's transcript is always kept with the flight. The recording and the recognizer's own text "
                "are kept only if you allow it."), name)
        self.assertEqual(quoted[0], quoted[1])


if __name__ == "__main__":
    unittest.main()
