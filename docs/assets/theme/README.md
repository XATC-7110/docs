# SeventyOneTen theme

The one source of the SeventyOneTen look for every site: the marketing site, the pilot site, the console, the data tool and the docs. Version **1.0.0**. The rules are in [../AGENTS.md](../AGENTS.md); the values are in [../tokens/tokens.json](../tokens/tokens.json), and `tokens.css` here is generated from them.

Open `demo.html` from disk to see every component, with switches for night or paper and soft or room.

## Files

| File | What |
|---|---|
| `tokens.css` | Generated. The raw palette and the semantic tokens, night as the base, paper under `prefers-color-scheme: light` (unless `data-theme="dark"`) and under `data-theme="light"`. |
| `fonts.css`, `fonts/` | Archivo 400, 500, 700, 800 and Archivo Narrow 600, self-hosted, with the OFL licences. No request leaves the site. |
| `shape-soft.css` / `shape-room.css` | Shape and type scale. **Link exactly one.** Soft: pill controls and tags, 8 px fields, 12 px cards, 40/24/18/16/14/12.5 px. Room: 6 px controls, 4 px tags, flush panes, 20/15/13/12/11 px. |
| `base.css` | The components, `s71-` classes in `@layer s71`. |
| `shell.css` | The tool shell (rail, status bar, pane, segmented switch, label-and-value grid), also `@layer s71`. Only the tools need it. |
| `theme.js` | A classic script: applies system, dark or light before first paint; remembers it under `s71.theme`. |
| `brand/` | Tile PNGs (plain 16 to 512, outlined 64 to 512), `tile.svg`, `tile-outlined.svg`, `favicon.ico`, `wordmark.html`. Copied from `logo/`; never redrawn. |
| `MANIFEST.json` | Every file's path and SHA-256, and the version. Written by `scripts/build_theme.py`. |

## How a site takes the theme

```html
<head>
  <script src="theme/theme.js"></script>           <!-- first, no defer: the theme is set before first paint -->
  <link rel="stylesheet" href="theme/tokens.css">
  <link rel="stylesheet" href="theme/fonts.css">
  <link rel="stylesheet" href="theme/shape-soft.css">   <!-- or shape-room.css; exactly one -->
  <link rel="stylesheet" href="theme/base.css">
  <link rel="stylesheet" href="theme/shell.css">        <!-- tools only -->
  <link rel="stylesheet" href="site.css">               <!-- the site's own CSS: unlayered, so it wins over @layer s71 -->
</head>
<body class="s71-page">
```

Keep the folder's layout (`fonts/` beside `fonts.css`). Do not edit a theme file in a site: change it upstream. The release asset is `seventyoneten-theme-vX.Y.Z.tar.gz`; a site checks its copy against `MANIFEST.json`.

## Tokens

Raw palette (never themed): `--s71-night`, `--s71-panel`, `--s71-paper`, `--s71-paper-card`, `--s71-teal`, `--s71-teal-deep`, `--s71-teal-hover` and so on, one per entry under `color` in `tokens.json`. Where a semantic name below would collide, the raw one gets `-night` (`--s71-line-night`, `--s71-deep-night`, `--s71-red-night`, ...).

Semantic (themed; use these in sites):

| Token | Use |
|---|---|
| `--s71-bg`, `--s71-surface`, `--s71-deep` | page, card or pane or header, inset or quiet surface |
| `--s71-text`, `--s71-text-2` | text, secondary text and labels |
| `--s71-accent`, `--s71-accent-hover`, `--s71-on-accent`, `--s71-accent-soft` | links and primary button, hover, text on the accent, a tint for a selected or hovered row, DERIVED from the accent (not a palette colour; night 0.12, paper 0.10). Body text sits on it; **accent text is not placed on it on paper** (4.0:1) |
| `--s71-line`, `--s71-line-strong` | hairlines, a button's border |
| `--s71-danger-text`, `--s71-danger-bg` | **errors only** |
| `--s71-warn-text`, `--s71-warn-bg`, `--s71-ok-bg` | warnings, ok notices |
| `--s71-chrome-bg`, `--s71-chrome-deep`, `--s71-chrome-line`, `--s71-chrome-text`, `--s71-chrome-text-2`, `--s71-chrome-accent`, `--s71-chrome-accent-soft` | **Chrome: the same value in both themes (night).** The header reads `chrome-bg`; the rail and status bar read `chrome-deep`. Use them for nothing else |
| `--s71-focus`, `--s71-live` | the focus ring, the live mark |
| `--s71-red` | **graphics only**, never text |
| `--s71-shadow`, `--s71-tile-plain-display`, `--s71-tile-outlined-display` | a floating thing; which tile shows |

Also: `--s71-font`, `--s71-font-label`, `--s71-font-mono`, `--s71-tracking-label`, `--s71-tracking-title`, `--s71-lh-body`, `--s71-lh-tight`, `--s71-s-1` to `--s71-s-7` (4 px grid), `--s71-t-fast`. Set by the shape files: `--s71-r-control`, `--s71-r-tag`, `--s71-r-field`, `--s71-r-card`, `--s71-r-dialog`, `--s71-r-seg`, `--s71-r-seg-item`, `--s71-card-border`, `--s71-card-divider`, `--s71-card-pad`, `--s71-fs-display|title|h2|body|small|label`, and the button, field and tag padding tokens.

## Classes

- Page and type: `s71-page`, `s71-display`, `s71-title`, `s71-h2`, `s71-small`, `s71-mono`, `s71-num` (tabular figures; right-aligned in a table cell), `s71-label`, `s71-link`.
- Brand: `s71-wordmark` (see `brand/wordmark.html`), `s71-tile` with `s71-tile--plain` and `s71-tile--outlined` (put both images in; the theme shows the outlined one on night), `s71-header` with `__brand`, `__nav`, `__end`.
- Buttons: `s71-btn`, `--primary`, `--quiet`, `--sm`.
- Tags: `s71-tag`, `--live`, `--info`, `--warning`, `--problem`; `s71-live`. A tag's words must say the thing; the tone only backs them.
- Forms: `s71-field-group`, `s71-field` (set `aria-invalid="true"` for an error), `s71-hint`, `s71-error`, `s71-notice` with `--warning`, `--problem`.
- Content: `s71-table` (in `s71-table-wrap`), `s71-card` and `--live`, `s71-dialog` (on `<dialog>`) with `__actions`.
- Shell: `s71-shell`, `__main`, `s71-rail` with `__link` (`aria-current` for the current one), `__badge`, `__me`; `s71-work`, `s71-pane` with `__head`, `__body`; `s71-status` with `__k`; `s71-segs` with `__item` (`aria-pressed="true"` for the current one); `s71-kv`.

## Rules the theme keeps

**Chrome is night in both themes.** The header, the rail and the status bar do not turn paper (the live sites' header does not). They read only `--s71-chrome-*` tokens, the tile inside them is always the outlined one, and the wordmark, nav links, badge, account circle and live mark take the chrome colours. Page content under them follows the theme.

Red is for errors only, and colour is never the only signal (words, a glyph or a bar come with it). Strip red `#D64545` is graphics only. Teal `#2EC4B6` is for night; on paper the accent is `#1B746B`. The 71/10 tile never inverts; on night the outlined tile shows. There is no paper scope class.

## Changing it

Edit `tokens/tokens.json` (and record a colour change in `AGENTS.md`), then:

```bash
uv run --no-project python -I scripts/build_theme.py     # writes theme/tokens.css and MANIFEST.json
uv run --no-project python -I scripts/check_contrast.py  # WCAG AA for every declared pairing, both themes
uv run --no-project python -I scripts/package_theme.py   # dist/seventyoneten-theme-vX.Y.Z.tar.gz (+ .sha256)
```

Versions: patch for a fix that renames nothing, minor for a new token or component, major for a renamed or removed token or class. Update `themeVersion` in `tokens.json`.
