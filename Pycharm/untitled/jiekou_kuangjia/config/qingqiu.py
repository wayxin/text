
import requests
import unittest
from jiekou_kuangjia.data.duqu import shuju
class wind(unittest.TestCase):
    def denglu(self ,user ,passwd):
        sj=shuju()
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"

        payload = '{"phone":"%s","password":"%s","zone":"86","loginType":0,"isAuto":0,"deviceId":"ec:89:14:54:93:007"} ' % \
        (user ,passwd)
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'cache-control': "no-cache",
            'Postman-Token': "c1b0547a-8ee5-434b-a79c-bbe40861fcd7"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        res =response.json()
        return res
if __name__=='__main__':
    shu=shuju()
    for i in range(len(shu)):
        aa=wind().denglu(int(shu[i][0]),int(shu[i][1]))
        print(aa)