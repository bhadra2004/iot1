
import paho.mqtt.client as mqtt
import random
import json
import time

token = "pUQVVsBrHnVsVzrlE1pm"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(token)

client.connect("mqtt.eu.thingsboard.cloud", 1883)

client.loop_start()

while True:
    data = {
        "temperature": round(random.uniform(25, 35), 2),
        "humidity": round(random.uniform(40, 80), 2)
    }

    client.publish(
        "v1/devices/me/telemetry",
        json.dumps(data)
    )

    print("Published:", data)
    time.sleep(5)
