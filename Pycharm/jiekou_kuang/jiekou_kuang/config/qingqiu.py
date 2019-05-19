#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
from jiekou_kuang.data.duqu import Shuju

class jiekou_qingqiu():
    def denglu(self,user,passwd):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
        payload = '{"phone":"%s","password":"%s","zone":"86","loginType":0,"isAuto":0,"deviceId":"ec:89:14:54:93:007"}' % (
        user, passwd)
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'cache-control': "no-cache"
        }
        response = requests.post(url, data=payload, headers=headers)
        res = response.json()
        return res

if __name__ == '__main__':
    shu = Shuju().shuju()
    for i in range(len(shu)):
        aa = jiekou_qingqiu().denglu(int(shu[i][0]),int(shu[i][1]))
        print(aa)
