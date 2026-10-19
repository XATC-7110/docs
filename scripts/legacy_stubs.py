#!/usr/bin/env python3
"""Write redirect stubs for the pre-versioning page addresses.

Before the docs were versioned, every page lived at the root of the site
(``/docs/getting-started/``). Other repositories and the installed client link
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
  site's 404 page (its links are absolute, under ``/docs/<version>/``, so it needs
  no root ``assets/``).
* The stale files of the old build are deleted: ``sitemap.xml``, ``sitemap.xml.gz``
  and the ``search/``, ``assets/`` and ``stylesheets/`` folders. Each version has
  its own copies; the root ones would be a second, frozen search index and sitemap.

Standard library only.

    legacy_stubs.py --source <pages>/latest --dest <pages> --base-url https://xatc-7110.github.io/docs
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


def publish_404(source: Path, dest: Path) -> bool:
    """Copy the source's 404.html to the site root; False when the source has none."""
    page = source / "404.html"
    if not page.is_file():
        return False
    shutil.copyfile(page, dest / "404.html")
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
    ap.add_argument("--base-url", required=True, help="the site's address without the version, e.g. https://xatc-7110.github.io/docs")
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
    print("copied 404.html")
    for name in remove_stale_build(args.dest, args.alias):
        print(f"removed old {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
