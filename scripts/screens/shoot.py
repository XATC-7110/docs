"""Shoot a representative set of docs pages for a theme before/after check (SOT-260).
Usage: shoot.py <built-site-dir> <out-dir>
Serves the built site the way mike lays it out (the site under /1.0/, a versions.json at the root, so the version selector shows),
then for each page: night and paper (Material's own switch, set on <body>), at 1440 and 375 px, full page, plus the visible text,
the sideways scroll (scrollWidth - innerWidth), page errors and failed requests. Chromium from XATC_SHOOT_CHROMIUM."""
import functools, http.server, json, os, shutil, socketserver, sys, tempfile, threading
from pathlib import Path
from playwright.sync_api import sync_playwright

PAGES = {
    "home": "", "getting-started": "getting-started/", "settings": "settings/", "troubleshooting": "troubleshooting/",
    "install-mac": "install-mac/", "window": "window/", "how-it-works": "how-it-works/", "traffic": "traffic/",
    "clearance": "features/clearance/", "approach-card": "client/approach-card/",
}
SCHEMES = {"night": "slate", "paper": "default"}
WIDTHS = {1440: 900, 375: 812}

def serve(site: Path):
    root = Path(tempfile.mkdtemp())
    shutil.copytree(site, root / "1.0")
    (root / "versions.json").write_text(json.dumps([{"version": "1.0", "title": "1.0.0", "aliases": ["latest"]},
                                                   {"version": "0.9", "title": "0.9.0", "aliases": []}]))
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
    handler.log_message = lambda *a, **k: None
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}/1.0/"

def set_scheme(page, name):
    page.evaluate("""(s) => { const b = document.body; b.setAttribute('data-md-color-scheme', s);
        b.setAttribute('data-md-color-primary', 'custom'); b.setAttribute('data-md-color-accent', 'custom'); }""", name)
    page.wait_for_timeout(150)

def main(site, out):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    srv, base = serve(Path(site))
    report = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=os.environ.get("XATC_SHOOT_CHROMIUM"), args=["--no-sandbox"])
        for width, height in WIDTHS.items():
            for sname, scheme in SCHEMES.items():
                ctx = browser.new_context(viewport={"width": width, "height": height},
                                          color_scheme="dark" if sname == "night" else "light", reduced_motion="reduce")
                page = ctx.new_page()
                errors = []
                page.on("pageerror", lambda e: errors.append(f"pageerror {e}"))
                page.on("console", lambda m: errors.append(f"console {m.text}") if m.type == "error" else None)
                page.on("requestfailed", lambda r: errors.append(f"failed {r.url}"))
                page.on("response", lambda r: errors.append(f"http{r.status} {r.url}") if r.status >= 400 else None)
                for label, path in PAGES.items():
                    key = f"{label}-{sname}-{width}"
                    errors.clear()
                    page.goto(base + path, wait_until="networkidle")
                    set_scheme(page, scheme)
                    page.evaluate("document.fonts.ready")
                    page.screenshot(path=str(out / f"{key}.png"), full_page=True)
                    report[key] = {
                        "text": page.inner_text("body"),
                        "sideways": page.evaluate("document.documentElement.scrollWidth - window.innerWidth"),
                        "errors": [e for e in errors if "favicon" not in e],
                        "default_scheme": page.evaluate("document.body.getAttribute('data-md-color-scheme')") if False else None,
                    }
                # the search open (viewport shot)
                key = f"search-{sname}-{width}"
                page.goto(base + "features/clearance/", wait_until="networkidle"); set_scheme(page, scheme)
                (page.click("label.md-header__button[for=__search]") if width < 1000 else page.click("input.md-search__input")); page.fill("input.md-search__input", "readback")
                try: page.wait_for_selector(".md-search-result__item", timeout=6000)
                except Exception: pass
                page.wait_for_timeout(500)
                page.screenshot(path=str(out / f"{key}.png"))
                report[key] = {"text": page.inner_text(".md-search-result") if page.query_selector(".md-search-result") else "", "sideways": 0, "errors": []}
                # the version switcher open
                key = f"version-{sname}-{width}"
                page.goto(base + "features/clearance/", wait_until="networkidle"); set_scheme(page, scheme)
                page.wait_for_timeout(500)
                sel = page.query_selector(".md-version")
                shown = bool(sel and sel.is_visible())
                if not shown and width < 1000:
                    page.click("label.md-header__button[for=__drawer]"); page.wait_for_timeout(300)
                    sel = page.query_selector(".md-version"); shown = bool(sel and sel.is_visible())
                if shown:
                    try:
                        page.hover(".md-version", timeout=3000)
                    except Exception:
                        page.focus(".md-version__current", timeout=3000) if page.query_selector(".md-version__current") else None
                    page.wait_for_timeout(400)
                page.screenshot(path=str(out / f"{key}.png"))
                report[key] = {"text": page.inner_text(".md-version") if sel else "", "sideways": 0, "errors": [], "version_visible": shown}
                # the default scheme the site opens in (no stored choice)
                page.evaluate("localStorage.clear()")
                ctx.close()
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, color_scheme="light")
        pg = ctx.new_page(); pg.goto(base, wait_until="networkidle")
        report["_default_scheme_when_system_prefers_light"] = pg.evaluate("document.body.getAttribute('data-md-color-scheme')")
        report["_fonts"] = pg.evaluate("[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight)")
        report["_body_font"] = pg.evaluate("getComputedStyle(document.querySelector('.md-typeset')).fontFamily")
        browser.close()
    (out / "report.json").write_text(json.dumps(report, indent=1))
    srv.shutdown()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
