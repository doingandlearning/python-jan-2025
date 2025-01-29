"""
Learn how to fetch web content using Python. -> httpx // requests (http 1.1) -> http2
Extract and parse useful information from HTML. -> BeautifulSoup
Fetch and work with JSON APIs.
Understand ethical and legal considerations of web scraping. -> robots.txt
"""

import requests
import json

headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
response = requests.get("https://swapi.dev/api/people", headers=headers)

if response.status_code != 200:
    print(f"Failed to fetch data. Status code {response.status_code}")
    raise Exception()


data = response.json()
with open('data.json', 'w') as file:
    json.dump(data["results"], file, indent=2)
print(data["results"])
