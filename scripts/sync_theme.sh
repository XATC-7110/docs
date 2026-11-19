#!/usr/bin/env bash
# Take the SeventyOneTen theme (XATC-7110/brand, release asset seventyoneten-theme-v<version>.tar.gz) as a pinned copy.
# Downloads the asset with `gh release download`, checks its SHA-256, replaces docs/assets/theme/ with its
# files and rewrites theme.lock. Run only when someone upgrades the theme; CI never fetches anything (tests/test_theme_vendored.py
# checks the copied files against the theme's own MANIFEST.json). Never edit a file under docs/assets/theme/ by hand.
#
#   scripts/sync_theme.sh            # the version in theme.lock, checked against the pinned SHA-256
#   scripts/sync_theme.sh 1.1.0      # an upgrade: the new SHA-256 is computed and written to theme.lock
set -euo pipefail
cd "$(dirname "$0")/.."
LOCK=theme.lock
DEST=docs/assets/theme
locked_version="$(python3 -c "import json;print(json.load(open('$LOCK'))['version'])")"
locked_sha="$(python3 -c "import json;print(json.load(open('$LOCK'))['sha256'])")"
version="${1:-$locked_version}"
version="${version#v}"
asset="seventyoneten-theme-v${version}.tar.gz"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
gh release download "v${version}" --repo XATC-7110/brand --pattern "$asset" --dir "$work"
if command -v sha256sum >/dev/null 2>&1; then actual="$(sha256sum "$work/$asset" | cut -d' ' -f1)"; else actual="$(shasum -a 256 "$work/$asset" | cut -d' ' -f1)"; fi
if [ "$version" = "$locked_version" ] && [ "$actual" != "$locked_sha" ]; then
  echo "SHA-256 of $asset is $actual, but $LOCK pins $locked_sha. Not copied." >&2
  exit 1
fi
mkdir "$work/unpack"
tar -xzf "$work/$asset" -C "$work/unpack"
src="$work/unpack/seventyoneten-theme-v${version}"
[ -f "$src/MANIFEST.json" ] || { echo "no MANIFEST.json in $asset" >&2; exit 1; }
rm -rf "$DEST"
mkdir -p "$DEST"
cp -R "$src"/. "$DEST"/
printf '{"version": "%s", "sha256": "%s"}\n' "$version" "$actual" > "$LOCK"
echo "Theme $version copied to $DEST (sha256 $actual). Review the diff, run the tests and open a PR."
