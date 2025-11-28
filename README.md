# Real-Time Crypto Streaming Pipeline 🚀

## Overview
A high-performance streaming data pipeline that ingests, processes, and visualizes cryptocurrency trade data in real-time. Built to demonstrate Event-Driven Architecture using Redpanda (Kafka) and Docker.

## Architecture
**Flow:** `Python Producer` -> `Redpanda (Broker)` -> `Streamlit (Consumer/Dashboard)`


## Key Features
* **Real-Time Ingestion:** Handles continuous data streams using Apache Kafka protocol (Redpanda).
* **Live Visualization:** Dynamic dashboard updates instantly as new events arrive.
* **Microservices:** Decoupled architecture where Producer and Consumer run independently.
* **Zero-Install:** Fully containerized with Docker.

## Tech Stack
* **Broker:** Redpanda (Kafka compatible)
* **Visualization:** Streamlit
* **Language:** Python 3.9
* **Infrastructure:** Docker Compose

## How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/crypto-realtime-pipeline.git](https://github.com/YOUR_USERNAME/crypto-realtime-pipeline.git)
    ```
2.  **Start the cluster:**
    ```bash
    docker compose up --build -d
    ```
3.  **View the Dashboard:**
    * Open `http://localhost:8501` to see live charts.
    * Open `http://localhost:8080` to see the Redpanda Console.