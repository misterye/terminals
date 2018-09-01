#!/usr/bin/python
import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt
#import json
import os
import time
#import requests

sensor_data = {'temperature': 0, 'humidity':0}
client = mqtt.Client("sub_pub_test")

humidity, temperature = Adafruit_DHT.read_retry(11, 14)
humidity = round(humidity, 2)
temperature = round(temperature, 2)
sensor_data['temperature'] = temperature
sensor_data['humidity'] = humidity

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker.")
        global Connected
        Connected = True
    else:
        print("Connection failed.")

def on_message(client, userdata, message):
    print "Message received: " + message.payload
    if message.payload == "gxgadzt_temp":
        client.publish('devices/raspi/gxgadzt/fetch_val', sensor_data['temperature'])
    elif message.payload == "gxgadzt_hum":
        client.publish('devices/raspi/gxgadzt/fetch_val', sensor_data['humidity'])
    else:
        client.publish('devices/raspi/gxgadzt/fetch_val', 'NULL')

Connected = False

MQTT_HOST = '111.47.20.166'
port = 1883
user = ""
password = ""

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
#INTERVAL = 5
client.username_pw_set(user, password=password)
client.on_connect = on_connect
client.on_message = on_message
#next_reading = time.time()
# Connect to server using default MQTT port and 60 seconds keepalive interval
client.connect(MQTT_HOST, port=port)
client.loop_start()

while Connected != True:
    time.sleep(0.1)

client.subscribe("devices/raspi/gxgadzt/control")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
