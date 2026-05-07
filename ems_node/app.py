from flask import Flask, render_template_string
import paho.mqtt.client as mqtt
import threading

app = Flask(__name__)

# Global data storage
bess_data = {
    "soc": 0,
    "temperature": 0,
    "status": "OFFLINE"
}

# MQTT Logic
def on_message(client, userdata, message):
    import json
    global bess_data
    try:
        payload = json.loads(message.payload.decode("utf-8"))
        bess_data["soc"] = payload.get("soc", 0)
        bess_data["temperature"] = payload.get("temperature", 0)
        bess_data["status"] = "ACTIVE"
    except:
        pass

def start_mqtt():
    client = mqtt.Client()
    client.on_message = on_message
    try:
        client.connect("10.31.245.51", 1883, 60) # Broker IP from your logs
        client.subscribe("bess/status")
        client.loop_forever()
    except:
        print("MQTT Connection Failed")

# Modern UI Design (English Only)
HTML_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="2">
    <title>BESS | Control Center</title>
    <style>
        body { background: #050505; color: #00ff9d; font-family: 'Segoe UI', sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .dashboard { background: #111; padding: 40px; border-radius: 20px; border: 1px solid #00ff9d; box-shadow: 0 0 30px rgba(0, 255, 157, 0.2); }
        h1 { letter-spacing: 5px; color: #fff; text-shadow: 0 0 10px #00ff9d; margin-bottom: 30px; }
        .grid { display: flex; gap: 40px; }
        .stat-box { text-align: center; min-width: 200px; }
        .label { font-size: 14px; color: #888; text-transform: uppercase; margin-bottom: 10px; }
        .value { font-size: 60px; font-weight: bold; font-family: 'Courier New'; }
        .status { margin-top: 30px; font-size: 12px; padding: 5px 15px; border-radius: 50px; background: #222; }
    </style>
</head>
<body>
    <h1>SYSTEM MONITOR</h1>
    <div class="dashboard">
        <div class="grid">
            <div class="stat-box">
                <div class="label">Battery SOC</div>
                <div class="value">{{ data.soc }}%</div>
            </div>
            <div class="stat-box">
                <div class="label">Internal Temp</div>
                <div class="value">{{ data.temperature }}°C</div>
            </div>
        </div>
    </div>
    <div class="status">DEVICE STATUS: {{ data.status }}</div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_UI, data=bess_data)

if __name__ == "__main__":
    # Start MQTT in background
    threading.Thread(target=start_mqtt, daemon=True).start()
    # Start Web Server
    app.run(host='0.0.0.0', port=5001, debug=False)
