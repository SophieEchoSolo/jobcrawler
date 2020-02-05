import scrapy
import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.se/jobb/sok/?where=Stockholm__2C-Stockholms-l__C3__A4n'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ContentContainer')

print(results.prettify())