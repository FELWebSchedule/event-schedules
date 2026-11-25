from playwright.sync_api import sync_playwright

url = "https://hotwheelsmonstertruckslive.com/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    print("Testing browser access:", url)

    response = page.goto(
        url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    print("HTTP STATUS:", response.status)
    print("PAGE TITLE:", page.title())
    print("PAGE LENGTH:", len(page.content()))

    browser.close()
