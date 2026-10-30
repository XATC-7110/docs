"""SOT-119 (the owner, 2026-10-21: "It should be \"SeventyOneTen\"" and "xatc should not be anywhere"): no text a reader can
see says "xatc". The one exception is the names of files and folders the reader handles, which the client keeps on disk
(client#148 renamed everything the pilot sees: the window, the Start menu, Settings > Apps, the banner and its messages).
They stay literal where a page tells the reader what to click or type (ALLOWED below).
Not scanned: URLs and repository names are not in the pages, AGENTS.md and README.md are developer docs, the stylesheet's
file name and the comments in mkdocs.yml and the CSS are code.
Run: python -m unittest discover -s tests -v"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Literal names, exactly as they are on disk.
ALLOWED = [
    "xatc-agent-setup-<version>.exe",           # the Windows installer's file name
    "xatc-agent-<version>-x86_64.AppImage",     # the Linux AppImage's file name
    "xatc-agent-client",                        # the settings folder, the log file, the credential name
    "Drag **xatc-agent** to your",              # the Mac app's file name in Finder (no localized display name is set)
    "Open **xatc-agent** from Applications, not from the disk image.",   # the same, in Applications
    "switch on **xatc-agent** (it may be listed as SeventyOneTen).",   # the microphone setting can list the Finder name (Mac)
    "Drag **xatc-agent** from Applications to the Trash.",  # removing the Mac app
    "xatc-agent-<version>-arm64.dmg",           # the Mac disk image's file name
    "its file name, `xatc-agent`;",             # the Mac app's file name, said once on the Mac page
    "~/.xatc-agent/session.json",               # the flight's session file, which the client keeps in the home folder
    "Custom Data/xatc-traffic/CSL",             # the folder Bluebell goes in, as the client's window names it
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
