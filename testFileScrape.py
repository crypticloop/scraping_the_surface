from scrapeFunction import *

scrape_for_headlines_complicated('https://news.ycombinator.com/news',"tr","athing","a","storylink")
scrape_for_headlines_simple('https://www.bbc.co.uk/news',"h3","class","gs-c-promo-heading__title")
scrape_for_headlines_simple('https://news.sky.com/',"span","class","sdc-site-tile__headline-text")
scrape_for_headlines_simple('https://www.telegraph.co.uk/',"h3","class","list-of-entities__item-body-headline")
