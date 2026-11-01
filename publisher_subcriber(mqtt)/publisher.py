
import paho.mqtt.client as mqtt
import random
import json
import time

broker = "broker.hivemq.com"
topic = "mca/iot/sensor/demo2026"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(broker, 1883)
client.loop_start()

while True:
    data = {
        "temperature": round(random.uniform(25, 35), 2),
        "humidity": round(random.uniform(40, 80), 2)
    }

    client.publish(topic, json.dumps(data))
    print("Published:", data)
    time.sleep(5)
