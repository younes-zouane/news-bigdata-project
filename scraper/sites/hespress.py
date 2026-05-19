import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_hespress():

    BASE_URL = "https://www.hespress.com"

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

    articles = soup.find_all("article")

    for article in articles[:5]:

        try:

            title = article.get_text(strip=True)

            if not title:
                continue

            article_data = {
                "title": title,
                "author": "Unknown",
                "date": str(datetime.now()),
                "category": "Morocco",
                "content": title,
                "source": "Hespress",
                "url": BASE_URL
            }

            articles_data.append(article_data)

            print(f"[HESPRESS] {title}")

        except Exception as e:

            print("Hespress Error:", e)

    return articles_data