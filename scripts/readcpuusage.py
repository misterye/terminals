import os
import requests
import json
from time import sleep

try:
    while True:
        f = open('cpu_usage_data', 'r')
        lines = f.readlines()
        linestring = lines[0].split()
        usagestr = linestring[1][0]
        usagenum = float(usagestr)
        newusagestr = str(usagenum)+'%'
        data = {'pi_temp':newusagestr, 'pi_name':'rnldmz'}
        print data
        try:
            response = requests.post('http://139.224.114.83:8019/getTemp', json=data)
        except requests.RequestException as e:
            print(e.message)
        f.close()
        sleep(6)
except KeyboardInterrupt:
    pass
