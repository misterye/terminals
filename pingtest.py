#!/usr/bin/python

import os
from time import sleep

while True:
    response = os.system('ping -c 30 10.8.0.1')
    internet_resp = os.system('ping -c 30 114.114.114.114')
    #print("The response is: %s" % response)

    if response == 0:
        print 'Connected!'
    elif internet_resp == 0:
        #print response
        print 'OpenVPN is down.'
        #sudoPasswd = '33927569'
        #command = 'systemctl restart openvpn'
        #os.system('echo %s | sudo -S %s' % (sudoPasswd, command))
        #os.system('sudo reboot')
        os.system('sudo systemctl restart openvpn')
    else:
        print 'Disconnected!'
        os.system('sudo reboot')

    sleep(3600)
