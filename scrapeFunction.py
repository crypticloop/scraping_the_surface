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
        tempString = CleanText(headline.find(elementTagType, {"class":elementClassName}).text)
        if tempString:
            print(tempString)
            headlineTitles.append(tempString)

    client.close()
    return headlineTitles

def scrape_for_headlines_simple(url, spanTagType, firstClassifierType, spanClassName):
    client = uReq(url)
    html = client.read()
    soupPart = soup(html, "html.parser")

    headlines = soupPart.findAll(spanTagType,{firstClassifierType:spanClassName})
    headlineTitles = []

    for headline in headlines:
        tempString = CleanText(headline.text)
        if tempString:
            print(tempString)
            headlineTitles.append(tempString)

    client.close()
    return headlineTitles

def CleanText(inputString):
    inputString = inputString.replace(",", "|")
    inputString = inputString.strip()
    return inputString
