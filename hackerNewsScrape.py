from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

timeBeforeURL = time.time()
hackerNewsUrl = 'https://news.ycombinator.com/news'
timeAfterURL = time.time()

print("Time for URL: ", timeAfterURL - timeBeforeURL)

timeBeforeClient = time.time()
hackerNewsClient = uReq(hackerNewsUrl)
timeAfterClient = time.time()

print("Time for Client: ", timeAfterClient - timeBeforeClient)

timeBeforeRead = time.time()
hackerNewsHtml = hackerNewsClient.read()
timeAfterRead = time.time()

print("Time for Read: ", timeAfterRead - timeBeforeRead)

hackerNewsSoup = soup(hackerNewsHtml, "html.parser")


print(hackerNewsSoup.title)

hackerNewsClient.close()
