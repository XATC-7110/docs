# xatc-agent documentation

Source for the xatc-agent documentation site: AI air traffic control for X-Plane 12.

**The site: <https://xatc-7110.github.io/docs/>**

It is written for pilots: how to install and configure the client, how to fly with it, and what the controllers can do. Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Build locally

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

`mkdocs build --strict` fails on a broken internal link or a page missing from the nav.

## Publish

The site lives on the `gh-pages` branch, which GitHub Pages serves ("Deploy from a branch": `gh-pages`, `/ (root)`). From an up-to-date, clean `main`:

```bash
scripts/publish-docs.sh             # mkdocs build --strict, then mkdocs gh-deploy
scripts/publish-docs.sh --no-push   # the same, on the local gh-pages branch only
```

The `docs` workflow runs the strict build on every pull request and publishes on every push to `main`.

## Layout

| Path | What |
|---|---|
| `docs/index.md`, `getting-started.md`, `first-flight.md` | What it is, installing, a flight gate to gate |
| `docs/window.md`, `settings.md` | The client's window and its settings |
| `docs/features/` | What ATC can do, position by position |
| `docs/client/` | The window's cards: the approach plan, parking, PDC, your X-Plane's data |
| `docs/privacy.md`, `troubleshooting.md`, `how-it-works.md` | Your data, when something goes wrong, the design in one page |
| `docs/assets/` | Screenshots, taken from the client's demo data, and the logo |
| `docs/stylesheets/xatc.css` | The look: the client window's colours, dark first |
