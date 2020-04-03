from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

client = uReq("https://www.nfl.com/teams")
html = client.read()
soupPart = soup(html, "html.parser")

arr = soupPart.findAll("h2")

print(len(arr))
