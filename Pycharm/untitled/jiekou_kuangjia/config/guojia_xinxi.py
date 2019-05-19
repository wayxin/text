#! /usr/bin/python
#- -*- coding:utf-8 -*-
import unittest
import requests
class guojia(unittest.TestCase):
    def gj(self):
        url = "http://120.132.8.33:9000/api/Others/GetCountryList"

        payload = ""
        headers = {
        'Content-Type': "application/json",
        'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
        'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
        'Language': "zh_CN",
        'APIVersion': "3.0",
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "2b3e7ca9-cf52-4445-b6e7-d08884ece88c,e23e116a-b4c1-427d-823b-aa2868635817",
        'Host': "120.132.8.33:9000",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        res=response.json()
        return res

if __name__ == '__main__':
    aa = guojia().gj()
    print(aa)