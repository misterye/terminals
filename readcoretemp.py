import os
import sys
import time
from time import sleep
import paho.mqtt.client as mqtt

MQTT_HOST = '111.47.20.166'
INTERVAL = 2
clientstr = 'xiqidongshu_test'
client = mqtt.Client()
next_reading = time.time()
client.connect(MQTT_HOST, 1883, 60)
client.loop_start()
try:
    while True:
        os.system('sensors > /home/test/scripts/newcoretemp')
        f = open('newcoretemp', 'r')
        lines = f.readlines()
        linestring = lines[6].split()
        tempstr = linestring[2][1:5]
        tempnum = float(tempstr)-10
        #newtempstr = str(tempnum)
        humidity = 30
        client.publish('devices/raspi/clientstr', clientstr)
        client.publish('devices/raspi/temperature', tempnum)
        client.publish('devices/raspi/humidity', humidity)
        next_reading += INTERVAL
        sleep_time = next_reading - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
        f.close()
except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()
