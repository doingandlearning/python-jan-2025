import requests
from bs4 import BeautifulSoup

url = "https://bbc.co.uk/news"

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

if response.status_code != 200:
    print(f"Something went wrong: {response.status_code}")
    raise Exception()

soup = BeautifulSoup(response.text, "html.parser")

h3s = soup.find_all("h3")

print([h3.text for h3 in h3s])
