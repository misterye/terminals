import requests
import os
from time import sleep

while True:
    wx_user_post = {"ToUserName":"gh_6bbed8a1f0c3", "FromUserName":"oiesgwrElMXVhP31KrFJjVkKAXsI", "CreateTime":"1514856291", "MsgType":"text", "Content":"hbwwdmz", "MsgId":"6506258228402476962"}
    response = requests.post('http://139.224.114.83:5000/getStatus', json=wx_user_post)
    if response.ok:
        print 'ok'
    else:
        print 'Request post to server failed.'
    sleep(10800)
