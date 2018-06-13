#!/usr/bin/python
import os
import sys
from time import sleep
import numpy as np

try:
    while True:
        os.system("mosquitto_pub -h 111.47.20.166 -t testdata -m test.txt")
        sleep(1)
except KeyboardInterrupt:
    pass
