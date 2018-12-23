from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

def scrape_for_headlines_complicated(url, spanTagType, spanClassName, elementTagType, elementClassName):
    client = uReq(url)
    html = client.read()
    soupPart = soup(html, "html.parser")

    headlines = soupPart.findAll(spanTagType,{"class":spanClassName})
    headlineTitles = []

    for headline in headlines:
        headlineTitles.append(headline.find(elementTagType, {"class":elementClassName}).text)

    for headlineTitle in headlineTitles:
        headlineTitle = headlineTitle.replace(",", "|")

    for x in range(0,len(headlineTitles)):
        print(headlineTitles[x])

    client.close()

def scrape_for_headlines_simple(url, spanTagType, firstClassifierType, spanClassName):
    client = uReq(url)
    html = client.read()
    soupPart = soup(html, "html.parser")

    headlines = soupPart.findAll(spanTagType,{firstClassifierType:spanClassName})
    headlineTitles = []

    for headline in headlines:
        headlineTitles.append(headline.text)

    for x in range(0,len(headlineTitles)):
        CleanText(headlineTitles[x])

    client.close()

def CleanText(inputString):
    inputString = inputString.replace(",", "|")
    inputString = inputString.strip()
    print(inputString)
