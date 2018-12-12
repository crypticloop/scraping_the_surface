# There is a similar set up for the other tabs - expand this further if there's time

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

url = 'https://news.sky.com/'
client = uReq(url)
html = client.read()
soup = soup(html, "html.parser")

filename = "skyResults.csv"
f= open(filename, "w")

headlines = soup.findAll("span",{"class":"sdc-site-tile__headline-text"})
headlineTitles = []

for headline in headlines:
    headlineTitles.append(headline.text)
    print(headline.text)

for headlineTitle in headlineTitles:
    f.write(headlineTitle.replace(",", "|") + "\n")

f.close()
client.close()
