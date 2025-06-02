from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

items = ["iPhone", "MacBook", "iPad", "AirPods"]

while True:
    order = {
        "order_id": random.randint(1000, 9999),
        "item_id": random.choice(items),
        "qty": random.randint(1, 5),
        "timestamp": datetime.utcnow().isoformat()
    }
    producer.send("orders_stream", order)
    print(f"✅ Sent order: {order}")
    time.sleep(2)
