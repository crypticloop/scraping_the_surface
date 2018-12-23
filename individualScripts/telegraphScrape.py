## Explore different tags, and whether these can be scraped as well

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

url = 'https://www.telegraph.co.uk/'
client = uReq(url)
html = client.read()
soup = soup(html, "html.parser")

filename = "telegraphResults.csv"
f= open(filename, "w")

headlines = soup.findAll("h3",{"class":"list-of-entities__item-body-headline"})
headlineTitles = []

for headline in headlines:
    headlineTitles.append(headline.text)
    print(headline.text)

for headlineTitle in headlineTitles:
    f.write(headlineTitle.replace(",", "|") + "\n")

f.close()
client.close()
