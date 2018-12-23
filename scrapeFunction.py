from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

def scrape_for_headlines_complicated(url, spanTagType, spanClassName, elementTagType, elementClassName):
    client = uReq(url)
    html = client.read()
    soupPart = soup(html, "html.parser")

    # filename = "hackerNewsResults.csv"
    # f= open(filename, "w")

    headlines = soupPart.findAll(spanTagType,{"class":spanClassName})
    headlineTitles = []

    for headline in headlines:
        headlineTitles.append(headline.find(elementTagType, {"class":elementClassName}).text)

    for headlineTitle in headlineTitles:
        # f.write(headlineTitle.replace(",", "|") + "\n")
        print(headlineTitle.replace(",", "|") + "\n")

    # f.close()
    client.close()

def scrape_for_headlines_simple(url, spanTagType, firstClassifierType, spanClassName):
    client = uReq(url)
    html = client.read()
    soupPart = soup(html, "html.parser")

    # filename = "hackerNewsResults.csv"
    # f= open(filename, "w")

    headlines = soupPart.findAll(spanTagType,{firstClassifierType:spanClassName})
    headlineTitles = []

    for headline in headlines:
        headlineTitles.append(headline.text)

    for headlineTitle in headlineTitles:
        # f.write(headlineTitle.replace(",", "|") + "\n")
        print(headlineTitle.replace(",", "|") + "\n")

    # f.close()
    client.close()
