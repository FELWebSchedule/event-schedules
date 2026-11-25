from playwright.sync_api import sync_playwright
from urllib.parse import urlparse, urljoin

URL = "https://hotwheelsmonstertruckslive.com/event/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    response = page.goto(
        URL,
        wait_until="domcontentloaded",
        timeout=90000
    )

    page.wait_for_timeout(10000)

    print("HTTP STATUS:", response.status)

    links = page.locator("a[href]").evaluate_all(
        "(elements) => elements.map(a => ({text: a.innerText.trim(), href: a.href}))"
    )

    events = {}

    for link in links:
        href = urljoin(URL, link["href"])
        parsed = urlparse(href)
        path = parsed.path.rstrip("/")

        if (
            parsed.netloc == urlparse(URL).netloc
            and path.startswith("/event/")
            and path != "/event"
        ):
            clean_url = parsed.scheme + "://" + parsed.netloc + path + "/"
            events[clean_url] = link["text"]

    print("TOTAL EVENT LINKS:", len(events))

    for href, text in sorted(events.items()):
        print(text, "|", href)

    browser.close()
