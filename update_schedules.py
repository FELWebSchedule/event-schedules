
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

url = "https://hotwheelsmonstertruckslive.com/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    response = page.goto(
        url,
        wait_until="domcontentloaded",
        timeout=60000
    )
    page.wait_for_timeout(5000)

    print("HTTP STATUS:", response.status)

    soup = BeautifulSoup(page.content(), "html.parser")
    links = {}

    for link in soup.find_all("a", href=True):
        href = link["href"]
        label = link.get_text(" ", strip=True)

        if href not in links:
            links[href] = label

    print("TOTAL UNIQUE LINKS:", len(links))

    for href, label in links.items():
        print(f"{label} | {href}")

    browser.close()
