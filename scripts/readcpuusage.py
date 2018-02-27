import os
import sys
import time
from time import sleep
import paho.mqtt.client as mqtt

MQTT_HOST = '111.47.20.166'
INTERVAL = 2
client = mqtt.Client()
next_reading = time.time()
client.connect(MQTT_HOST, 1883, 60)
client.loop_start()
try:
    while True:
        f = open('cpu_usage_data', 'r')
        lines = f.readlines()
        linestring = lines[0].split()
        usagestr = linestring[1][0]
        usagenum = float(usagestr)
        client.publish('devices/raspi/rnldmz/temperature', usagenum)
        next_reading += INTERVAL
        sleep_time = next_reading - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
        f.close()
except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()
