import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker.")
        global Connected
        Connected = True
    else:
        print("Connection failed.")

def on_message(client, userdata, message):
    print "Message received: " + message.payload

broker = '111.47.20.166'
Connected = False
client = mqtt.Client("testsub")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)
client.loop_start()
while Connected != True:
    time.sleep(0.1)
client.subscribe("devices/raspi/gxgadzt/#")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print "exiting..."
    client.disconnect()
    client.loop_stop()
