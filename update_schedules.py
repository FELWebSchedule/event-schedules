import requests
from bs4 import BeautifulSoup

BASE = "https://hotwheelsmonstertruckslive.com"

urls = [
    BASE + "/event/billings-mt-2027/",
    BASE + "/event/london-uk-2027/",
    BASE + "/event/coming-soon-asuncion/"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

for url in urls:
    print("\n" + "=" * 70)
    print("EVENT URL:", url)

    response = requests.get(
        url, headers=headers, timeout=60
    )

    print("HTTP STATUS:", response.status_code)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    print("PAGE CONTENT:")
    print(soup.get_text(separator="\n", strip=True))
