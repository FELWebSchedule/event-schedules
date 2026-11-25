from urllib.request import Request, urlopen
from urllib.error import HTTPError

urls = [
    "https://hotwheelsmonstertruckslive.com/",
    "https://hotwheelsmonstertruckslive.com/event/",
    "https://hotwheelsmonstertruckslive.com/wp-json/"
]

for url in urls:
    print("\nTesting:", url)
    try:
        request = Request(url, headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "text/html,application/json,*/*"
        })
        with urlopen(request, timeout=30) as response:
            print("SUCCESS:", response.status)
            print("Bytes:", len(response.read()))
    except HTTPError as error:
        print("HTTP ERROR:", error.code)
    except Exception as error:
        print("ERROR:", str(error))
