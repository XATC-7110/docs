#!/usr/bin/env bash
set -euo pipefail

# Publishes one docs release to the gh-pages branch, which GitHub Pages serves
# ("Deploy from a branch": gh-pages, / (root)).
#
#   scripts/deploy-versioned.sh v1.2.3             # build, deploy version 1.2, push gh-pages
#   scripts/deploy-versioned.sh v1.2.3 --no-push   # the same, on the local gh-pages branch only
#
# A release vX.Y.Z deploys the version X.Y (titled X.Y.Z) and moves the alias `latest`,
# which is the default: the site root redirects to it. Re-releasing a patch replaces X.Y.
# The old, unversioned page addresses (/docs/getting-started/) keep working: each gets a
# redirect stub to /docs/latest/ (scripts/legacy_stubs.py), committed with the deploy.
#
# The CI workflow (.github/workflows/docs-release.yml) is the normal way to run this; it
# calls it from a checkout of the release tag. Run it by hand only with --no-push, to look.
#
# Environment (all optional): MIKE, MKDOCS (commands), PAGES_BRANCH (default gh-pages),
# SITE_BASE_URL (default https://xatc-7110.github.io/docs).

PUSH=true
TAG=""
for arg in "$@"; do
  case "$arg" in
    --no-push) PUSH=false ;;
    v*) TAG="$arg" ;;
    *) echo "usage: $(basename "$0") vX.Y.Z [--no-push]" >&2; exit 2 ;;
  esac
done
if [[ ! "$TAG" =~ ^v([0-9]+)\.([0-9]+)\.([0-9]+)$ ]]; then
  echo "deploy-versioned.sh: the release tag must look like v1.2.3 (stable releases only), got '${TAG}'" >&2
  exit 2
fi
VERSION="${BASH_REMATCH[1]}.${BASH_REMATCH[2]}"
TITLE="${BASH_REMATCH[1]}.${BASH_REMATCH[2]}.${BASH_REMATCH[3]}"

cd "$(dirname "${BASH_SOURCE[0]}")/.."
MIKE="${MIKE:-mike}"
MKDOCS="${MKDOCS:-mkdocs}"
BRANCH="${PAGES_BRANCH:-gh-pages}"
BASE_URL="${SITE_BASE_URL:-https://xatc-7110.github.io/docs}"
ALIAS=latest

if [[ -n "$(git status --porcelain)" ]]; then
  echo "deploy-versioned.sh: working tree is dirty: commit first" >&2
  exit 1
fi

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

# A strict build first: a broken internal link or a page missing from the nav stops the deploy.
"$MKDOCS" build --strict -d "$WORK/check"

# mike commits to the local gh-pages branch (it creates it from origin/gh-pages when it is
# not there yet); nothing is pushed until the stubs are committed too.
"$MIKE" deploy --branch "$BRANCH" --title "$TITLE" --update-aliases \
  --message "Publish docs ${TITLE} (${TAG})" "$VERSION" "$ALIAS"
"$MIKE" set-default --branch "$BRANCH" "$ALIAS"

# The stubs are written in a throwaway clone of the branch, then fast-forwarded back, so
# the working tree of this checkout is never switched.
git clone --quiet --branch "$BRANCH" --single-branch "$(pwd)" "$WORK/pages"
python3 scripts/legacy_stubs.py --source "$WORK/pages/$ALIAS" --dest "$WORK/pages" --base-url "$BASE_URL" > "$WORK/stubs.txt"
echo "legacy stubs: $(wc -l < "$WORK/stubs.txt" | tr -d ' ') pages"
git -C "$WORK/pages" config user.name "$(git config user.name || echo github-actions[bot])"
git -C "$WORK/pages" config user.email "$(git config user.email || echo 41898282+github-actions[bot]@users.noreply.github.com)"
git -C "$WORK/pages" add -A
if ! git -C "$WORK/pages" diff --cached --quiet; then
  git -C "$WORK/pages" commit --quiet -m "Redirect the old page addresses to ${ALIAS} (${TAG})"
  git -C "$WORK/pages" push --quiet origin "HEAD:refs/heads/${BRANCH}"
fi

if $PUSH; then
  git push origin "${BRANCH}:${BRANCH}"
else
  echo "--no-push: ${BRANCH} is committed locally, not pushed"
fi
