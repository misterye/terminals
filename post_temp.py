import os
from time import sleep

while True:
    os.system('/usr/bin/python /home/pi/Scripts/read_temp.py')
    sleep(10)
