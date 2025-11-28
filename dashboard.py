import streamlit as st
from confluent_kafka import Consumer
import json
import pandas as pd
import time

# 1. Page Config
st.set_page_config(page_title="Live Crypto Feed", layout="wide")
st.title("🚀 Real-Time Crypto Dashboard")

# 2. Setup Kafka Consumer
# We use 'redpanda:29092' because we are inside Docker
conf = {
    'bootstrap.servers': 'redpanda:29092',
    'group.id': 'dashboard-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['crypto_prices'])

# 3. Create Layout (Two Columns)
col1, col2 = st.columns(2)
with col1:
    st.subheader("Bitcoin (BTC)")
    btc_placeholder = st.empty()

with col2:
    st.subheader("Ethereum (ETH)")
    eth_placeholder = st.empty()

# 4. Data Storage (Keep last 50 points)
data_buffer = {'BTC': [], 'ETH': []}

st.success("Connected to Redpanda Stream! Waiting for data...")

# 5. The Infinite Consumer Loop
try:
    while True:
        msg = consumer.poll(0.5) # Check for new messages
        
        if msg is None:
            continue
        if msg.error():
            st.error(f"Error: {msg.error()}")
            continue

        # Parse the message
        record = json.loads(msg.value().decode('utf-8'))
        symbol = record['symbol']
        price = record['price']
        
        # We only care about BTC and ETH for this demo
        if symbol in ['BTC', 'ETH']:
            data_buffer[symbol].append(price)
            # Keep only last 50 prices to keep chart clean
            if len(data_buffer[symbol]) > 50:
                data_buffer[symbol].pop(0)

            # Update Charts
            if symbol == 'BTC':
                with btc_placeholder:
                    st.line_chart(data_buffer['BTC'])
            elif symbol == 'ETH':
                with eth_placeholder:
                    st.line_chart(data_buffer['ETH'])

except KeyboardInterrupt:
    pass
finally:
    consumer.close()