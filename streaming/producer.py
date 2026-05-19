from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open("../data/bronze/articles.json", "r", encoding="utf-8") as f:

    articles = json.load(f)

for article in articles:

    producer.send("news-topic", article)

    print("Sent:", article["title"])

    time.sleep(2)

producer.flush()