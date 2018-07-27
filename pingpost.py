#!/usr/bin/python

import os
from time import sleep
import paho.mqtt.client as mqtt

MQTT_HOST = '111.47.20.166'
client = mqtt.Client()

#while True:
sleep(300)
internet_resp = os.system('ping -c 10 114.114.114.114')
sleep(15)
response = os.system('ping -c 10 10.8.0.1')
sleep(15)
if internet_resp == 0:
    client.connect(MQTT_HOST, 1883, 60)
    client.publish('devices/raspi/gxgadzt/status', 1)
    if response != 0:
        os.system('sudo systemctl restart openvpn')
else:
    os.system('sudo reboot')
    #sleep(30)
