#!/usr/bin/env python3
"""Write redirect stubs for the pre-versioning page addresses.

Before the docs were versioned, every page lived at the root of the site
(``/getting-started/`` since the site moved to its own domain, docs.7110atc.com, SOT-87; before that
``/docs/getting-started/`` on github.io). Other repositories and the installed client link
there, so each of those addresses must keep working. After ``mike deploy`` has
put the built pages under ``latest/``, this walks that folder and writes, at the
same relative path in the site root, a small page that sends the reader to
``<base>/latest/<page>/``, keeping the ``?query`` and the ``#anchor``.

Only ``<page>/index.html`` files in the root are written. Version folders
(``1.0/``, ``latest/``, ...), ``versions.json`` and the root ``index.html``
(mike's own redirect) are never touched.

Two more things are done at the root, because the old unversioned build left its
files there:

* ``404.html`` is copied from the source, so a mistyped address still shows the
  site's 404 page (its links are absolute, under ``/<version>/``, so it needs
  no root ``assets/``). A few lines are added to the root copy: an address that still begins with ``/docs/``
  (the old github.io project path) is sent to the same address without it. GitHub already drops that
  prefix when it redirects github.io to the custom domain; this is the belt to those braces.
* The stale files of the old build are deleted: ``sitemap.xml``, ``sitemap.xml.gz``
  and the ``search/``, ``assets/`` and ``stylesheets/`` folders. Each version has
  its own copies; the root ones would be a second, frozen search index and sitemap.

* ``CNAME`` (``--cname docs.7110atc.com``) is written at the root when it is missing or different:
  GitHub Pages serves the custom domain only while the branch root has it.

Standard library only.

    legacy_stubs.py --source <pages>/latest --dest <pages> --base-url https://docs.7110atc.com --cname docs.7110atc.com
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote

# Folders of the built site that hold files, not pages.
NOT_PAGES = {"assets", "stylesheets", "search"}
# A root folder named like a version: a stub is never written into one.
VERSION_DIR = re.compile(r"^[0-9]+(\.[0-9]+)*$")

# What the old, unversioned build left at the root. Each version folder has its own copies.
STALE_FILES = ("sitemap.xml", "sitemap.xml.gz")
STALE_DIRS = ("search", "assets", "stylesheets")

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirecting...</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace({target_js} + location.search + location.hash);</script>
</head>
<body>
<p>This page has moved to <a href="{target}">{target}</a>.</p>
</body>
</html>
"""


def pages(source: Path) -> list[str]:
    """Page paths of a built site as 'a/b' (no trailing slash); the home page is ''."""
    found = []
    for index in sorted(source.rglob("index.html")):
        rel = index.parent.relative_to(source)
        if rel.parts and rel.parts[0] in NOT_PAGES:
            continue
        found.append("/".join(rel.parts))
    return found


def version_dirs(dest: Path) -> set[str]:
    """Names of the root folders that are versions or aliases, from versions.json."""
    names: set[str] = set()
    manifest = dest / "versions.json"
    if manifest.is_file():
        for entry in json.loads(manifest.read_text(encoding="utf-8")):
            names.add(entry["version"])
            names.update(entry.get("aliases", []))
    return names


def write_stubs(source: Path, dest: Path, base_url: str, alias: str = "latest") -> list[str]:
    """Write a stub for every page of ``source`` under ``dest``; return the relative paths written."""
    base = base_url.rstrip("/")
    reserved = version_dirs(dest) | {alias}
    written = []
    for page in pages(source):
        if not page:  # the root index.html belongs to mike's redirect
            continue
        first = page.split("/")[0]
        if first in reserved or VERSION_DIR.match(first):
            raise SystemExit(f"legacy_stubs: page '{page}' would write into the version folder '{first}'")
        target = f"{base}/{alias}/{quote(page)}/"
        out = dest / page / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            TEMPLATE.format(target=html.escape(target, quote=True), target_js=json.dumps(target)),
            encoding="utf-8",
        )
        written.append(f"{page}/index.html")
    return written


# Added to the root 404: an address under the old github.io project path (/docs/...) goes to the same one at the root.
OLD_PREFIX_SCRIPT = (
    "<script>(function () { var p = location.pathname;"
    ' if (p.indexOf("/docs/") !== 0) return;'
    " var rest = p.slice(5);"
    # Never an open redirect: a second leading / or \\ after the prefix (/docs//evil.example/x) would be a
    # protocol-relative address, so it is refused, and the origin is always put in front.
    ' if (rest.charAt(1) === "/" || rest.charAt(1) === "\\\\") return;'
    " location.replace(location.origin + rest + location.search + location.hash); })();</script>"
)


def publish_404(source: Path, dest: Path) -> bool:
    """Copy the source's 404.html to the site root, with the old-prefix redirect; False when the source has none."""
    page = source / "404.html"
    if not page.is_file():
        return False
    text = page.read_text(encoding="utf-8")
    head = re.search(r"<head[^>]*>", text)
    if head:
        text = text[: head.end()] + OLD_PREFIX_SCRIPT + text[head.end():]
    else:
        text = OLD_PREFIX_SCRIPT + text
    (dest / "404.html").write_text(text, encoding="utf-8")
    return True


def ensure_cname(dest: Path, domain: str) -> bool:
    """Make ``dest/CNAME`` say ``domain``; True when it had to be written (missing or different)."""
    path = dest / "CNAME"
    if path.is_file() and path.read_text(encoding="utf-8").strip() == domain:
        return False
    path.write_text(domain + "\n", encoding="utf-8")
    return True


def remove_stale_build(dest: Path, alias: str = "latest") -> list[str]:
    """Delete the old unversioned build's sitemap, search index, assets and stylesheets at the root."""
    reserved = version_dirs(dest) | {alias}
    removed = []
    for name in STALE_FILES + STALE_DIRS:
        if name in reserved:
            raise SystemExit(f"legacy_stubs: '{name}' is a version or alias folder: refusing to delete it")
        path = dest / name
        if path.is_symlink() or path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)
        else:
            continue
        removed.append(name)
    return removed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--source", required=True, type=Path, help="the built pages of the latest version")
    ap.add_argument("--dest", required=True, type=Path, help="the site root (the gh-pages checkout)")
    ap.add_argument("--base-url", required=True, help="the site's address without the version, e.g. https://docs.7110atc.com")
    ap.add_argument("--cname", help="the custom domain: written to CNAME at the site root when missing or different")
    ap.add_argument("--alias", default="latest")
    args = ap.parse_args(argv)
    if not args.source.is_dir() or not args.dest.is_dir():
        print("legacy_stubs: --source and --dest must be existing folders", file=sys.stderr)
        return 2
    written = write_stubs(args.source, args.dest, args.base_url, args.alias)
    if not written:
        print("legacy_stubs: no pages found in the source: refusing to publish a site with no old links", file=sys.stderr)
        return 1
    # The root 404 first: the old root assets are deleted only once nothing at the root needs them.
    if not publish_404(args.source, args.dest):
        print("legacy_stubs: the source has no 404.html: refusing to delete the old root files", file=sys.stderr)
        return 1
    for rel in written:
        print(f"stub {rel}")
    if args.cname and ensure_cname(args.dest, args.cname):
        print(f"wrote CNAME {args.cname}")
    print("copied 404.html")
    for name in remove_stale_build(args.dest, args.alias):
        print(f"removed old {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
