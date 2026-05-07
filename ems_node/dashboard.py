import streamlit as st
import pandas as pd
import paho.mqtt.client as mqtt
import json
import time

# Dashboard Configuration
st.set_page_config(page_title="BESS Monitoring Dashboard", layout="wide")
st.title("🔋 BESS Real-Time Monitoring System")

# Initialize Session State for Data
if 'bess_data' not in st.session_state:
    st.session_state.bess_data = pd.DataFrame(columns=['Time', 'SOC', 'Temp'])

# MQTT Setup
def on_message(client, userdata, message):
    data = json.loads(message.payload.decode())
    new_entry = {
        'Time': time.strftime("%H:%M:%S"),
        'SOC': data['soc'],
        'Temp': data['temperature']
    }
    # Keep only the last 20 readings for the chart
    st.session_state.bess_data = pd.concat([st.session_state.bess_data, pd.DataFrame([new_entry])]).tail(20)

client = mqtt.Client()
client.on_message = on_message
client.connect("10.31.245.118", 1883, 60)
client.subscribe("bess/data")
client.loop_start()

# --- Dashboard UI Elements ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Battery Charge (SOC %)")
    if not st.session_state.bess_data.empty:
        st.line_chart(st.session_state.bess_data.set_index('Time')['SOC'])

with col2:
    st.subheader("System Temperature (°C)")
    if not st.session_state.bess_data.empty:
        st.area_chart(st.session_state.bess_data.set_index('Time')['Temp'])

# Metrics
if not st.session_state.bess_data.empty:
    latest = st.session_state.bess_data.iloc[-1]
    m1, m2 = st.columns(2)
    m1.metric("Current SOC", f"{latest['SOC']}%")
    m2.metric("Temperature", f"{latest['Temp']}°C")

# Auto-refresh the UI
time.sleep(2)
st.rerun()
