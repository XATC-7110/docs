# xatc-agent documentation

Source for the xatc-agent documentation site: AI air traffic control for X-Plane 12.

**The site: <https://docs.7110atc.com/>** (the product's home is <https://7110atc.com>)

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

A release `vX.Y.Z` deploys the version `X.Y` (titled `X.Y.Z`). When it is the newest stable tag it also moves the alias `latest` to it and keeps `latest` as the default, so <https://docs.7110atc.com/> redirects to `/latest/`. Releasing a patch (`v1.0.1`) replaces `1.0`; a new minor (`v1.1.0`) adds a version. The theme's version selector lists them all.

Cut a docs release from a pushed, up-to-date `main` with the release skill (`gh release create` tags the remote `main`, so unpushed commits are not in the release). Docs releases go through it because a hook blocks a raw `gh release create`. Keep the notes file outside `docs/` (the skill's default path is inside the site's source folder; `pending-release-*.md` there is ignored by git and left out of the site as a safety net, but do not rely on it):

```bash
bash ~/.claude/skills/release/release.sh init   v1.0.0 /tmp/docs-release-v1.0.0.md   # scaffold the notes
# fill the notes in, then:
bash ~/.claude/skills/release/release.sh create v1.0.0 /tmp/docs-release-v1.0.0.md
```

`release.sh` requires a compare link in the notes. The **first** release has nothing earlier to compare with, so its link is `compare/v1.0.0...v1.0.0`. Later releases compare with the previous tag (`compare/v1.0.0...v1.1.0`).

Publishing the release starts the `docs-release` workflow, which deploys the tag. What it does, and does not do:

- A **stable** release (`vX.Y.Z`) deploys. A **prerelease** (`v1.0.0-rc.1`) deploys nothing, a draft does nothing until it is published, and a bare tag does nothing.
- To deploy a published stable release again, run the `docs-release` workflow by hand (Actions > docs-release > Run workflow) with its tag. It checks that the tag is `vX.Y.Z` and that GitHub says the release is published, not a draft and not a prerelease. **`latest` moves only to the newest stable tag**: re-deploying an older release (`v1.0.0` after `v1.1.0`) replaces its own version folder, leaves `latest` on the newest, and says so in the run's output.
- The old, unversioned page addresses (`/getting-started/`) keep working: each is a redirect stub to `/latest/<page>/`, keeping the `#anchor`, written by `scripts/legacy_stubs.py` into the same push as the deploy. A page later removed from the docs keeps its old root address, so look at it when you remove a page. The same step puts `latest`'s `404.html` at the site root (its links are absolute, under `/<version>/`; the root copy also sends any address that still begins with `/docs/`, the old github.io project path, to the same address without it) and deletes the old unversioned build's root `sitemap.xml`, `sitemap.xml.gz`, `search/`, `assets/` and `stylesheets/`; each version folder has its own.
- **`CNAME`**: the root of `gh-pages` must hold a `CNAME` file saying `docs.7110atc.com`, or GitHub Pages stops serving the custom domain. Setting the domain in the repository's Pages settings commits one, and mike leaves it alone, but the deploy script checks it anyway (`legacy_stubs.py --cname`) and writes it in the same commit when it is missing or different. `SITE_DOMAIN` overrides the domain.
- Never run `mkdocs gh-deploy`: it replaces the whole `gh-pages` branch and would delete every version.

To look at what a deploy would write, without pushing anything: `scripts/deploy-versioned.sh v1.0.0 --no-push` (with `mike` installed; the local `gh-pages` branch is updated, the remote is not).

## The custom domain (docs.7110atc.com, SOT-87)

The owner, 2026-10-20: "Do SOT-87 and make sure the docs site is available at docs.7110atc.com". The site is GitHub Pages from the `gh-pages` branch, so with the custom domain its root is the root of that branch: versions live at `/1.0/` and `/latest/`, not under `/docs/`. Three things have to be true, **in this order**, before the first release after the move:

1. The DNS record: `docs.7110atc.com` CNAME `xatc-7110.github.io` (XATC-7110/dns, the Route 53 zone `7110atc.com`).
2. The repository's Pages setting: Settings > Pages > Custom domain `docs.7110atc.com`, then **Enforce HTTPS** once the certificate is ready.
3. A docs release, only after both: its redirect stubs and the sitemap point at the new address.

GitHub redirects `xatc-7110.github.io/docs/<page>` to `docs.7110atc.com/<page>` (the project path drops), which lands on the old-address stubs and so on `/latest/<page>/`.

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
| `tests/` | Tests of the stub generator, of the deploy script against a throwaway repository (the `CNAME` file), and of the site's addresses (`python -m unittest discover -s tests`) |
| `.github/workflows/` | `docs` (build and tests on every pull request and push), `docs-release` (deploy on a published stable release) |
