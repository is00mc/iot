from bs4.element import Script
import requests
from bs4 import BeautifulSoup
import sys

dev = sys.argv[1]
domain = sys.argv[2]

url = f"http://{dev}.{domain}"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

results = soup.find_all("script")

print(results)
