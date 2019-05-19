#！ /usr/bin/Python
#* -*- coding:utf-8 -*-
import requests
import json
import unittest
import xlrd
def xx():
    xinx=[]
    f=xlrd.open_workbook('AA.xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        xinx.append(sheet.row_values(i))
    print(xinx)
    return xinx
xx()

class grxx(unittest.TestCase):
    gx=xx()
    print(gx)
    def geren(self,gg,GG):
        url = "http://120.132.8.33:9000/api/Account/GetUserInfo"

        querystring = '{"accountGuid":"%s","countryGuid":"%s"}' % (gg,GG)

        payload = ""
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'accessToken': "71d57dbbb35e442e8656f024a3981b67",
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "a86387f8-ab7a-46ff-ad45-6f2f83f99a4c,8dc1cdb2-771a-40db-9c31-c9a73832834a",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        res = response.json()
        return res

    def test_one(self):
        one=self.geren(self.gx[0][0],self.gx[0][1])
        self.assertEqual(one['code'],0)
    def test_tuo(self):
        tuo=self.geren(self.gx[1][0],self.gx[1][1])
        self.assertNotEqual(tuo['msg'],'K')
if __name__ == '__main__':
    unittest.main()