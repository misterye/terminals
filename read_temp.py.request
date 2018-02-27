import requests
import os

os.system('/opt/vc/bin/vcgencmd measure_temp > /home/pi/terminals/temp_log.log')
with open('/home/pi/terminals/temp_log.log','r') as templog:
    temp = templog.readline()
newtemp = temp[5:9]
# post temperature json to server
data_from_pi = {'pi_temp':newtemp, 'pi_name':'hbwwdmz'}
try:
    response = requests.post('http://139.224.114.83:8019/getTemp', json=data_from_pi)
except requests.RequestException as e:
    print(e.message)
