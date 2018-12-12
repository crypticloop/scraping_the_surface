from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

url = 'https://news.ycombinator.com/news'

client = uReq(url)


html = client.read()


soup = soup(html, "html.parser")

headlines = soup.findAll("tr",{"class":"athing"})

print()
print("Information on the headlines:")
print()
print("Number of headlines:", len(headlines))
print()

print(headlines[0])

client.close()
