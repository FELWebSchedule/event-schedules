
import re
from urllib.request import Request, urlopen

url = "https://hotwheelsmonstertruckslive.com/"

request = Request(url, headers={
    "User-Agent": "Mozilla/5.0"
})

with urlopen(request, timeout=60) as response:
    html = response.read().decode("utf-8")

events = sorted(set(re.findall(
    r'https://hotwheelsmonstertruckslive\.com/event/[^"\'<>\s]+',
    html
)))

print("Website retrieved successfully")
print("Event links found:", len(events))

for event in events[-10:]:
    print(event)

if not events:
    raise RuntimeError("No event links found")
