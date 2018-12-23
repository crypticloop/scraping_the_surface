from scrapeFunction import *

print(scrape_for_headlines_complicated('https://news.ycombinator.com/news',"tr","athing","a","storylink"))
print(scrape_for_headlines_simple('https://www.bbc.co.uk/news',"h3","class","gs-c-promo-heading__title"))
print(scrape_for_headlines_simple('https://news.sky.com/',"span","class","sdc-site-tile__headline-text"))
print(scrape_for_headlines_simple('https://www.telegraph.co.uk/',"h3","class","list-of-entities__item-body-headline"))
