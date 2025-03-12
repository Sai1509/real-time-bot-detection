import numpy as np
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def simulate_data():
    while True:
        data = {
            'user_id': int(np.random.randint(1000, 9999)),
            'login_attempts': int(np.random.randint(1, 10)),
            'location': str(np.random.choice(['USA', 'India', 'China', 'Brazil'])),
            'time_spent_seconds': int(np.random.randint(1, 600)),
            'device': str(np.random.choice(['mobile', 'web', 'tablet'])),
            'is_fraud': int(np.random.choice([0, 1], p=[0.95, 0.05]))
        }
        producer.send('user_logs', data)
        print(f"Sent: {data}")
        time.sleep(1)

simulate_data()
