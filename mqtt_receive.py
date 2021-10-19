import paho.mqtt.client as mqtt
import random
import time

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))

client = mqtt.Client("TestNodeYes")

client.connect("192.168.1.110")

client.subscribe("node_red_out")

client.on_message = on_message

client.loop_forever()
