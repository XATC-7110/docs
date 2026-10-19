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

## Releasing the docs

The site is versioned with [mike](https://github.com/jimporter/mike) and **is published only by a release of this repository**. A push to `main` and a pull request run the strict build and the tests (`docs` workflow) and deploy nothing.

A release `vX.Y.Z` deploys the version `X.Y` (titled `X.Y.Z`), moves the alias `latest` to it and keeps `latest` as the default, so <https://xatc-7110.github.io/docs/> redirects to `/docs/latest/`. Releasing a patch (`v1.0.1`) replaces `1.0`; a new minor (`v1.1.0`) adds a version. The theme's version selector lists them all.

Cut a docs release from an up-to-date `main` with the release skill. Docs releases go through it because a hook blocks a raw `gh release create`. Keep the notes file outside `docs/` (the skill's default path is inside the site's source folder):

```bash
bash ~/.claude/skills/release/release.sh init   v1.0.0 /tmp/docs-release-v1.0.0.md   # scaffold the notes
# fill the notes in, then:
bash ~/.claude/skills/release/release.sh create v1.0.0 /tmp/docs-release-v1.0.0.md
```

Publishing the release starts the `docs-release` workflow, which deploys the tag. What it does, and does not do:

- A **stable** release (`vX.Y.Z`) deploys. A **prerelease** (`v1.0.0-rc.1`) deploys nothing, a draft does nothing until it is published, and a bare tag does nothing.
- To deploy a published stable release again, run the `docs-release` workflow by hand (Actions > docs-release > Run workflow) with its tag. It checks that the tag is `vX.Y.Z` and that GitHub says the release is published, not a draft and not a prerelease.
- The old, unversioned page addresses (`/docs/getting-started/`) keep working: each is a redirect stub to `/docs/latest/<page>/`, keeping the `#anchor`, written by `scripts/legacy_stubs.py` into the same push as the deploy. A page later removed from the docs keeps its old root address, so look at it when you remove a page.
- Never run `mkdocs gh-deploy`: it replaces the whole `gh-pages` branch and would delete every version.

To look at what a deploy would write, without pushing anything: `scripts/deploy-versioned.sh v1.0.0 --no-push` (with `mike` installed; it commits to a local `gh-pages` branch only).

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
| `scripts/deploy-versioned.sh`, `scripts/legacy_stubs.py` | The release deploy (mike) and the redirect stubs for the old page addresses |
| `tests/` | Tests of the stub generator (`python -m unittest discover -s tests`) |
| `.github/workflows/` | `docs` (build and tests on every pull request and push), `docs-release` (deploy on a published stable release) |
