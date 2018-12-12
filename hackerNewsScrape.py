from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

hackerNewsUrl = 'https://news.ycombinator.com/news'

hackerNewsClient = uReq(hackerNewsUrl)

hackerNewsHtml = hackerNewsClient.read()

hackerNewsSoup = soup(hackerNewsHtml, "html.parser")

print(hackerNewsSoup.title)

hackerNewsClient.close()
