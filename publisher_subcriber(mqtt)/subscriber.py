
import paho.mqtt.client as mqtt
import json

broker = "broker.hivemq.com"
topic = "mca/iot/sensor/demo2026"

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Temperature:", data["temperature"], "C")
    print("Humidity:", data["humidity"], "%")
    print("-----------------------")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect(broker, 1883)
client.subscribe(topic)

print("Waiting for messages...")
client.loop_forever()
