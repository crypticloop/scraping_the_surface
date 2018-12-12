# What to scrape

## FANG

There are lots of websites that might be useful to scrape. The initial thoughts are to go for a big website such as one of the FANG network:

* Facebook
* Apple
* Netflix
* Google

 However, most of these have APIs so text scraping would be a convoluted way around quite a simple task. Therefore, going to go for a target which is a bit less established, so that the web scraping tool built is actually useful.

## Hackernews

This [website](https://news.ycombinator.com/news) posts links to news on various technical topics. It's styling is simple which is promising, and it is relevant to the idea of web scraping, which is to gather information quickly and efficiently.

Once information is scraped from Hackernews, analysis can be carried out into the following:

* Links to common websites, which can indicate:
  * High activity on this website's part
  * Popularity of a website as a source of information on technical topics
* Sentiment of news titles, giving a general **mood** score for the front page at any one time (using NLP)

## Glassdoor

Quite a large website, but one that only offers a private API (_might be wrong, limited digging done_). There is valuable information here on how different companies are viewed by their employees. There is the potential to identify threat actors against a business by looking for and singling out **angry** feedback against a certain company (using NLP).
