import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_bbc():

    BASE_URL = "https://www.bbc.com/news"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        BASE_URL,
        headers=headers
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    articles_data = []

    headlines = soup.find_all("h2")

    for h in headlines[:5]:

        try:

            title = h.get_text(strip=True)

            if not title:
                continue

            article_data = {
                "title": title,
                "author": "BBC",
                "date": str(datetime.now()),
                "category": "International",
                "content": title,
                "source": "BBC",
                "url": BASE_URL
            }

            articles_data.append(article_data)

            print(f"[BBC] {title}")

        except Exception as e:

            print("BBC Error:", e)

    return articles_data