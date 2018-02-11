#!/usr/bin/python

import os
from time import sleep

while True:
    response = os.system('ping -c 30 10.8.0.1')
    #print("The response is: %s" % response)

    if response == 0:
        print 'Connected!'
    else:
        print 'Disconnected!'
        os.system('sudo systemctl restart openvpn')
        sleep(5)
        new_response = os.system('ping -c 10 10.8.0.1')
        if new_response == 0:
            print 'Connected!'
        else:
            print 'Disconnected!'
            os.system('sudo reboot')

    sleep(3600)
