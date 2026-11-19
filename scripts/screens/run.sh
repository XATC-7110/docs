#!/usr/bin/env bash
# Build the site the way CI does (pip install -r requirements.txt; mkdocs build --strict) and shoot it. Run inside idealab/client-tests:2
# with the repo at /home/tester/c:  scripts/screens/run.sh <out-dir>
set -euo pipefail
cd "$(dirname "$0")/../.."
uv venv -q --clear .venv-shoot && . .venv-shoot/bin/activate
uv pip install -q -r requirements.txt playwright
mkdocs build --strict -d site-shoot
XATC_SHOOT_CHROMIUM=${XATC_SHOOT_CHROMIUM:-/usr/local/bin/chromium} python scripts/screens/shoot.py site-shoot "$1"
