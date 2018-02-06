import requests
import os

os.system("sensors > /home/nibey/scripts/temperature.log && sed -n '7p' /home/nibey/scripts/temperature.log > /home/nibey/scripts/core0temp.log")

with open('/home/nibey/scripts/core0temp.log','r') as templog:
    temp = templog.readline()

newtemp = temp[15:19]
print newtemp

data_from_pi = {'pi_temp':newtemp, 'pi_name':'sony'}
response = requests.post('http://139.224.114.83:8086/getTemp', json=data_from_pi)
if response.ok:
    print 'ok'
else:
    print 'Request post to server failed.'
