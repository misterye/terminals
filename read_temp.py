#!/usr/bin/python
import sys
import paho.mqtt.client as mqtt
import os
import time
from time import sleep

MQTT_HOST = '111.47.20.166'
INTERVAL = 2
client = mqtt.Client()
next_reading = time.time()
client.connect(MQTT_HOST, 1883, 60)
client.loop_start()
try:
    while True:
        os.system('/opt/vc/bin/vcgencmd measure_temp > /home/pi/terminals/temp_log.log')
        with open('/home/pi/terminals/temp_log.log','r') as templog:
            temp = templog.readline()
        tempstr = temp[5:9]
        tempnum = float(tempstr)
        client.publish('devices/raspi/hbwwdmz/temperature', tempnum)
        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()
