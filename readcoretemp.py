import os
import requests
import json
from time import sleep

try:
    while True:
        os.system('sensors > /home/test/scripts/newcoretemp')
        f = open('newcoretemp', 'r')
        lines = f.readlines()
        linestring = lines[6].split()
        tempstr = linestring[2][1:5]
        tempnum = float(tempstr)-10
        newtempstr = str(tempnum)
        #print newtempstr
        data = {'pi_temp':newtempstr, 'pi_name':'xiqidongshu_test'}
        #print data
        try:
            response = requests.post('http://139.224.114.83:8019/getTemp', json=data)
        except requests.RequestException as e:
            print(e.message)
        f.close()
        sleep(10)
except KeyboardInterrupt:
    pass
