FROM python:3.9-slim

# Turn off buffering so we can see logs immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# CHANGED THIS LINE: Copy everything (producer.py AND dashboard.py)
COPY . .

CMD ["python", "producer.py"]