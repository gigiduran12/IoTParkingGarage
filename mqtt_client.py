import paho.mqtt.client as mqtt
import random
import time
import json


floor_count = 5
spot_count = 50
status_range_max = 12*1000 #12M
status_range_min = 0

client = mqtt.Client("TestNode")


while True:
	for floor in range(1,floor_count+1):
		for spot in range(1,spot_count+1):
			client.connect("192.168.1.110")
			
			status = random.randint(status_range_min,status_range_max)

			timestamp = int(time.time())

			data_dict = {"node":spot,
						"garage":floor,
						"status":status,
						"timestamp":timestamp
						}

			data_string = json.dumps(data_dict)
			print(data_string)
			client.publish("node_red",data_string, qos=1)
			#time.sleep(2)
		time.sleep(10)
	#time.sleep(60)
