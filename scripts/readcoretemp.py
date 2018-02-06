import os
import requests
import json
from time import sleep

try:
    while True:
        os.system('sensors > /home/nibey/scripts/newcoretemp')
        f = open('newcoretemp', 'r')
        lines = f.readlines()
        linestring = lines[13].split()
        tempstr = linestring[2][1:5]
        tempnum = float(tempstr)-30
        newtempstr = str(tempnum)
        data = {'pi_temp':newtempstr, 'pi_name':'sony'}
        try:
            response = requests.post('http://139.224.114.83:8019/getTemp', json=data)
        except requests.RequestException as e:
            print(e.message)
        f.close()
        sleep(6)
except KeyboardInterrupt:
    pass
