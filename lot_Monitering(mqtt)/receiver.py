
import paho.mqtt.client as mqtt
import requests
import json

url = "https://wxwrolktzxqlxwxhsbtz.supabase.co/rest/v1/sensor_data"
key = "sb_publishable_E3CHxZ57Q_aTaNXpx1cR0Q_djba1JJ6"

headers = {
    "apikey": key,
    "Content-Type": "application/json"
}

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        response = requests.post(
            url, json=data, headers=headers, timeout=10
        )
        print("Received:", data)
        print("Database Status:", response.status_code)
        if response.status_code != 201:
            print(response.text)
    except Exception as e:
        print("Error:", e)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect("broker.hivemq.com", 1883)
client.subscribe("mca/iot/temperature/demo2026")

print("Waiting for MQTT messages...")
client.loop_forever()
