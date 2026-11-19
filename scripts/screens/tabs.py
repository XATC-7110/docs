"""Measure the top tab row: does every tab fit?  python scripts/screens/tabs.py <built-site> [extra-css]
Prints, per width, the tab strip's scrollWidth and clientWidth and the right edge of the last tab against the strip."""
import os, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(Path(__file__).parent))
from shoot import serve

def main(site, css=""):
    srv, base = serve(Path(site))
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("XATC_SHOOT_CHROMIUM"), args=["--no-sandbox"])
        for w in (1220, 1440, 1920):
            page = b.new_page(viewport={"width": w, "height": 900})
            page.goto(base + "features/clearance/", wait_until="networkidle")
            if css: page.add_style_tag(content=css)
            page.evaluate("document.fonts.ready"); page.wait_for_timeout(300)
            r = page.evaluate("""() => { const t = document.querySelector('.md-tabs'), l = t.querySelector('.md-tabs__list');
              const items = [...t.querySelectorAll('.md-tabs__item')]; const last = items[items.length-1].getBoundingClientRect();
              return {n: items.length, scrollWidth: t.scrollWidth, clientWidth: t.clientWidth, listScroll: l.scrollWidth, listClient: l.clientWidth,
                      lastRight: Math.round(last.right), stripRight: Math.round(t.getBoundingClientRect().right), visible: getComputedStyle(t).display !== 'none'} }""")
            print(w, r)
        b.close()
    srv.shutdown()
main(*sys.argv[1:])
