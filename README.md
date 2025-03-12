# Real-Time Fraud Detection Pipeline

### 🚀 **Project Overview**
This project demonstrates a comprehensive, end-to-end real-time fraud detection system utilizing Machine Learning, Kafka streaming, FastAPI, and Streamlit. It's designed specifically to identify fraudulent activities in real-time, suitable for applications like cloud account protection, spam prevention, and abuse detection, aligning closely with roles such as Google's Trust & Safety team.

## 🛠️ Project Structure
```
fraud-detection-project
├── generate_data.py      # Simulates real-time user log data
├── train_model.py        # Trains the ML model and saves to fraud_model.pkl
├── fraud_model.pkl       # Serialized ML model
├── main.py               # FastAPI server for real-time ML prediction
├── app.py                # Streamlit real-time dashboard visualization
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## 🔑 Features
- **Real-Time Data Streaming:** Kafka-based streaming of synthetic user logs.
- **Machine Learning:** Random Forest model trained to detect fraud with handling of class imbalance.
- **REST API:** Real-time predictions served through FastAPI.
- **Interactive Dashboard:** Streamlit-based real-time visualization of fraud predictions.
- **Cloud Integration:** Optional integration with Google Cloud BigQuery for persistent storage.

## ⚙️ Tech Stack
- Python
- Apache Kafka (Streaming)
- FastAPI (REST API)
- Scikit-learn (ML Model)
- Streamlit (Visualization)
- Google Cloud Platform (Optional integration with BigQuery)

## 🚀 Running the Project

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Kafka using Docker
```bash
docker run -p 2181:2181 -p 9092:9092 -e ADVERTISED_HOST=localhost -e ADVERTISED_PORT=9092 spotify/kafka
```

### Step 3: Simulate Streaming Data
```bash
python generate_data.py
```

### Step 3: Train the ML Model
```bash
python train_model.py
```

### Step 4: Start FastAPI Server
```bash
uvicorn main:app --reload
```

### Step 5: Run Streamlit Dashboard
```bash
streamlit run app.py
```

## 📊 Dashboard
Access your real-time predictions and visualizations:
- Dashboard URL: `http://localhost:8501`

## ⚡ Optional: BigQuery Integration
To save predictions to Google BigQuery, configure your GCP credentials and ensure you've created a dataset and table.

## 🎯 Use-Cases
- Real-time abuse and fraud detection
- Enterprise cloud security monitoring
- Trust & safety analytics

---

## 📌 Future Enhancements
- Integrate advanced model explainability tools (SHAP, LIME).
- Add automated alerting mechanisms.

---

© Sai Gowtham Movidi | Real-Time Fraud Detection Project

