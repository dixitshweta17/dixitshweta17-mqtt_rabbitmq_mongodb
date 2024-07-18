import json
import paho.mqtt.client as mqtt
import random 
import time

BROKER_ADDRESS = 'localhost'
TOPIC = 'staus/update'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # client.subscribe(TOPIC)
    client.subscribe("mqtt_queue")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# client.connect(BROKER_ADDRESS, 1883, 60)
client.connect("localhost", 1883, 60)
# client.loop_start()

while True:
    status = random.randint(0, 6)
    message = json.dumps({"status": status})
    client.publish("mqtt_queue", message)
    print("Published message:", message)  # Debug print
    time.sleep(1)
    client.loop_forever()

# client.loop_forever()


    