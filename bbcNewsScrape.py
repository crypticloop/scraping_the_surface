from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

url = 'https://www.bbc.co.uk/news'
client = uReq(url)
html = client.read()
soup = soup(html, "html.parser")

filename = "bbcResults.csv"
f= open(filename, "w")

headlines = soup.findAll("h3",{"class":"gs-c-promo-heading__title"})
headlineTitles = []

for headline in headlines:
    headlineTitles.append(headline.text)
    print(headline.text)

for headlineTitle in headlineTitles:
    f.write(headlineTitle.replace(",", "|") + "\n")

f.close()
client.close()
