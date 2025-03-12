from fastapi import FastAPI
from kafka import KafkaConsumer
import joblib
import pandas as pd
import json

app = FastAPI()

model = joblib.load('fraud_model.pkl')

# FIXED HERE (9092 instead of 9902)
consumer = KafkaConsumer(
    'user_logs',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

@app.get("/")
async def health_check():
    return {"status": "API running"}

@app.get("/predict-stream")
async def predict_stream():
    predictions = []
    for message in consumer:
        data = message.value
        df = pd.get_dummies(pd.DataFrame([data]).drop(['user_id', 'is_fraud'], axis=1))

        expected_cols = [
            'login_attempts', 'time_spent_seconds',
            'location_Brazil', 'location_China', 'location_India', 'location_USA',
            'device_mobile', 'device_tablet', 'device_web'
        ]

        for col in expected_cols:
            if col not in df.columns:
                df[col] = 0

        prediction = model.predict(df[expected_cols])[0]
        result = {'user_id': data['user_id'], 'is_fraud': int(prediction)}
        predictions.append(result)

        if len(predictions) >= 10:
            break
    return predictions
