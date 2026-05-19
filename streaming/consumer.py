from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'news-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:

    article = message.value

    print(article)