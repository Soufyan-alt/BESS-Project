import paho.mqtt.client as mqtt
import json

# Configuration
BROKER_IP = "10.31.245.118"
TOPIC = "bess/data"

def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        soc = data.get("soc")
        temp = data.get("temperature")
        
        print(f"\n[DATA RECEIVED] SOC: {soc}% | Temp: {temp}C")
        
        # --- Logic: Decision Making System ---
        if temp > 45:
            print(">>> ACTION: [CRITICAL] Overheating detected! Shutting down system.")
        elif soc < 20:
            print(">>> ACTION: [LOW BATTERY] Starting emergency charge.")
        elif soc > 90:
            print(">>> ACTION: [FULL CAPACITY] Battery full. Switching to discharge mode.")
        else:
            print(">>> STATUS: System operating normally.")
            
    except Exception as e:
        print(f"Error processing message: {e}")

client = mqtt.Client()
client.on_message = on_message

print(f"EMS Controller started. Monitoring {TOPIC}...")
client.connect(BROKER_IP, 1883, 60)
client.subscribe(TOPIC)
client.loop_forever()
