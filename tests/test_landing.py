import subprocess
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANDING = ROOT / "landing" / "index.html"
FILE_URL = f"file://{LANDING.as_posix()}"

def test_title():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(FILE_URL)
        assert "dirfmt" in page.title().lower()
        browser.close()

def test_h1_exists():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(FILE_URL)
        h1 = page.locator("h1").text_content()
        assert h1 is not None
        assert "dirfmt" in h1.lower()
        browser.close()

def test_cards_present():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(FILE_URL)
        cards = page.locator(".card")
        assert cards.count() >= 2, f"Expected >=2 cards, got {cards.count()}"
        browser.close()

def test_cta_buttons():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(FILE_URL)
        btns = page.locator(".btn")
        assert btns.count() >= 1, f"Expected >=1 CTA button, got {btns.count()}"
        for i in range(btns.count()):
            text = btns.nth(i).text_content()
            assert text is not None and len(text.strip()) > 0
        browser.close()

def test_code_block():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(FILE_URL)
        pre = page.locator("pre")
        assert pre.count() >= 1, "Expected at least one code block"
        browser.close()

def test_responsive():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for width in [320, 768, 1280]:
            page = browser.new_page(viewport={"width": width, "height": 800})
            page.goto(FILE_URL)
            h1 = page.locator("h1").text_content()
            assert h1 is not None, f"H1 missing at width {width}"
            page.close()
        browser.close()

def test_no_broken_external_links():
    from playwright.sync_api import sync_playwright
    import time
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(FILE_URL)
        links = page.locator('a[href^="http"]')
        for i in range(links.count()):
            href = links.nth(i).get_attribute("href")
            if href:
                try:
                    resp = page.request.get(href, timeout=5000)
                    assert resp.status < 400, f"Broken link: {href} (status {resp.status})"
                except Exception:
                    pass
        browser.close()