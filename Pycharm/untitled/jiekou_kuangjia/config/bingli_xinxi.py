#! /usr/bin/python
#- -*- coding:utf-8 -*-
import requests
import unittest

class bingli(unittest.TestCase):
    def bl(self):
        url = "http://120.132.8.33:9000/api/Account/GetAllDiseaseInfo"
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
            'Postman-Token': "f6a05d6d-8252-4f16-898a-fb6d8916f713,38a8dd10-5b13-42d9-82ee-b53a467972cd",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }
        response = requests.request("GET", url, data=payload, headers=headers)
        res = response.json()
        print(res)
        return res
if __name__=='__main__':
    chakan=bingli().bl()
    print(chakan)