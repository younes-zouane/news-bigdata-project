# News Big Data Pipeline

## Technologies
- Python
- BeautifulSoup
- Kafka
- Spark
- Streamlit
- Airflow
- Docker

## Pipeline
Scraping → Bronze → Silver → Gold → Dashboard

## Run

### Scraper
python scraper.py

### Dashboard
streamlit run app.py

### Kafka
docker-compose up -d