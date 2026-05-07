import paho.mqtt.client as mqtt
import time
import json
import random

BROKER_IP = "10.31.245.118"
TOPIC = "bess/data"

client = mqtt.Client()
client.connect(BROKER_IP, 1883, 60)

print("BESS Emulator is running. Sending data...")

while True:
    payload = {
        "soc": random.randint(15, 95),
        "temperature": random.randint(20, 50),
        "status": "active"
    }
    client.publish(TOPIC, json.dumps(payload))
    print(f"Published: {payload}")
    time.sleep(2)
