#!/usr/bin/python
import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt
#import json
import os
import time
#import requests

MQTT_HOST = '111.47.20.166'
# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL = 5
sensor_data = {'temperature': 0, 'humidity':0}
client = mqtt.Client()
next_reading = time.time()
# Connect to server using default MQTT port and 60 seconds keepalive interval
client.connect(MQTT_HOST, 1883, 60)
client.loop_start()
try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 14)
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)
        sensor_data['temperature'] = temperature
        sensor_data['humidity'] = humidity
        #client.publish('devices/raspi/test01/temperature', json.dumps(sensor_data['temperature']), 1)
        #client.publish('devices/raspi/test01/humidity', json.dumps(sensor_data['humidity']), 1)
        client.publish('devices/raspi/gxgadzt/temperature', sensor_data['temperature'])
        # if humidity needs to be monitored, publish it as a new topic
        #client.publish('devices/raspi/gxgadzt/humidity', sensor_data['humidity'])
        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()
