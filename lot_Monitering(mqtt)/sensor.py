
import paho.mqtt.client as mqtt
import random
import json
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("broker.hivemq.com", 1883)
client.loop_start()

while True:
    data = {
        "temperature": round(random.uniform(25, 35), 2),
        "humidity": round(random.uniform(40, 80), 2)
    }

    client.publish("mca/iot/temperature/demo2026", json.dumps(data))
    print("Published:", data)
    time.sleep(5)
