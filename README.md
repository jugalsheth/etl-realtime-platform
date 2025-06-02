# ⚡ Real-Time ETL Data Platform

A real-time, event-driven data platform powered by **Apache Kafka**, **PySpark Structured Streaming**, and **Streamlit**. This project simulates an e-commerce order pipeline where events like "order received" → "inventory deduction" → "low stock alert" are handled in near real-time — from ingestion to transformation to visualization.

---

## 🚀 Project Motivation

As a data engineer, I wanted to go beyond batch pipelines and build something closer to production-grade **streaming data systems**. This project was an opportunity to:

- Learn Apache Kafka and PySpark with real-time streaming
- Simulate practical event chains (order → inventory → alert)
- Visualize streaming metrics via Streamlit
- Deepen system design thinking for portfolio + interviews

This system is designed for **learning, showcasing, and demoing** real-time data processing in action.

---

## ✅ Functional Requirements

- Ingest simulated orders as Kafka messages
- Use PySpark to stream, transform, and deduplicate events
- Write transformed data to local CSV (simulating data lake)
- Visualize order metrics and stock alerts in Streamlit
- Show event flows (new orders, inventory stock, low-stock items)

---

## 📦 Non-Functional Requirements

- Lightweight, runs locally without external dependencies
- No database setup required (uses CSVs as sink)
- Modular code structure for easy expansion
- Uses virtual environment to isolate dependencies
- Handles large message bursts with structured streaming engine

---

## 🧠 System Design Overview

### Architecture

[ Kafka Producer (Python Script) ]
↓
[ Kafka Topic: orders_topic ]
↓
[ PySpark Structured Streaming Consumer ]
↓
[ Transform & Write CSV Files ]
↓
[ Streamlit Dashboard (Live Refresh) ]


---

## 📸 Sneak Peek

### 🔄 Kafka Producer

Simulates order events with random item + quantity every second.

### ⚙️ PySpark Consumer

Processes, filters, and appends events to CSV with low-stock alerts.

### 📊 Streamlit Dashboard

Real-time metrics including:
- 🔢 Orders per minute
- 📦 Inventory left per item
- 🚨 Low stock alerts

---

## 🛠 Local Setup

1. **Clone the repo**  

git clone https://github.com/jugalsheth/etl-realtime-platform.git
cd etl-realtime-platform
Set up virtual environment

python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

pip install -r requirements.txt
Start Kafka (if installed locally)
Make sure your Kafka server is running and a topic like orders_topic is created.


💡 Future Additions
Add Redis or Delta Lake as sink for better performance
Integrate alerting via email/Slack for low stock
Add REST API layer (FastAPI) to trigger new orders
Deploy dashboard + pipeline to cloud (e.g., AWS/GCP)
Build more event types (returns, payments, shipments)

🧑‍💻 Built With
Apache Kafka
PySpark
Streamlit
Python
Pandas

Faker (for simulating data)

---

Screenshots
![Screenshot 2025-06-01 at 8 15 20 PM](https://github.com/user-attachments/assets/32202339-b34d-4efc-9a8d-f39f0df71856)


👋 Author
## 👋 Author **[Jugal Sheth](https://www.linkedin.com/in/jugalsheth/)** — Open to feedback, collabs, and any ideas to improve this!
