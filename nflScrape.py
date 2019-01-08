from scrapeFunction import *
from searchForWordFrequency import *

allResults = []

allResults.extend(scrape_for_headlines_simple('https://www.nfl.com/teams',"span","style","color: rgb(123, 123, 123); font-family: \"Endzone Sans Light\", sans-serif; font-size: 12px; line-height: 100%;"))

print(allResults)
