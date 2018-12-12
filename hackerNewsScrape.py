from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

url = 'https://news.ycombinator.com/news'
client = uReq(url)
html = client.read()
soup = soup(html, "html.parser")

filename = "results.csv"
f= open(filename, "w")

headlines = soup.findAll("tr",{"class":"athing"})
headlineTitles = []

for headline in headlines:
    headlineTitles.append(headline.find("a", {"class":"storylink"}).text)

for headlineTitle in headlineTitles:
    f.write(headlineTitle.replace(",", "|") + "\n")

f.close()
client.close()
