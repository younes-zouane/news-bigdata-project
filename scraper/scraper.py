from sites.hespress import scrape_hespress
from sites.bbc import scrape_bbc

import json

all_articles = []

all_articles.extend(scrape_hespress())
all_articles.extend(scrape_bbc())

with open("../data/bronze/all_articles.json", "w") as f:
    json.dump(all_articles, f, indent=4)

print("All websites scraped successfully")