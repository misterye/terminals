#!/usr/bin/python
import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt
import json
import os
import time
import requests

MQTT_HOST = '111.47.20.166'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL = 2

sensor_data = {'temperature': 0, 'humidity':0}
client = mqtt.Client()
next_reading = time.time()
count = 0

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

        data_from_pi = {'pi_temp':str(temperature), 'pi_name':'gxgadzt'}
        #print data_from_pi
        #try:
        #    response = requests.post('http://139.224.114.83:8019/getTemp', json=data_from_pi)
        #except requests.RequestException as e:
        #    print(e.message)

        # Sending humidity and temperature data to server
##        print json.dumps(sensor_data['temperature'])
        client.publish('devices/raspi/temperature', json.dumps(sensor_data['temperature']), 1)
##        print json.dumps(sensor_data['humidity'])
        client.publish('devices/raspi/humidity', json.dumps(sensor_data['humidity']), 1)
#        print temperature
#        print(type(temperature))
#        client.publish('devices/raspi/temperature', temperature, qos=0, retain=False)
        next_reading += INTERVAL
        count += INTERVAL
        if count % 10 == 0:
            #print("Count: %s" % count)
            try:
                response = requests.post('http://139.224.114.83:8019/getTemp', json=data_from_pi)
            except requests.RequestException as e:
                print(e.message)
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()


        #print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
