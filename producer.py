import time
import random
import simplejson as json
from confluent_kafka import Producer
from faker import Faker

# CONFIGURATION:
# We use 'redpanda' because inside Docker, we talk to the service name, not localhost.
conf = {
    'bootstrap.servers': 'redpanda:29092', 
}

producer = Producer(conf)
fake = Faker()

def get_fake_crypto_data():
    """Generates a fake trade event"""
    return {
        "timestamp": time.time(),
        "symbol": random.choice(["BTC", "ETH", "SOL", "DOGE"]),
        "price": round(random.uniform(20000, 70000), 2),
        "volume": round(random.uniform(0.1, 5.0), 4),
        "id": fake.uuid4()
    }

def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result."""
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

print("Starting Crypto Stream... Press Ctrl+C to stop.")

try:
    while True:
        data = get_fake_crypto_data()
        
        # Send data to the 'crypto_prices' topic
        producer.produce(
            'crypto_prices', 
            key=data['symbol'], 
            value=json.dumps(data).encode('utf-8'),
            callback=delivery_report
        )
        
        # Force the data to send immediately
        producer.flush()
        
        # Wait 1 second (Simulating real-time data)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping stream...")