#



# import requests
# import unittest

#url = "http://127.0.0.1:5000/login"
#
#payload = "username=zhangsan&password=123"
#headers = {
#             'Content-Type': "application/x-www-form-urlencoded",
#             'User-Agent': "PostmanRuntime/7.11.0",
#             'Accept': "*/*",
#             'Cache-Control': "no-cache",
#             'Postman-Token': "81df2b36-61c3-4977-b7ca-44d584a622e1,9c26ca3e-23eb-4ee7-92a8-67fc270c72aa",
#             'Host': "127.0.0.1:5000",
#             'accept-encoding': "gzip, deflate",
#             'content-length': "30",
#             'Connection': "keep-alive",
#             'cache-control': "no-cache"
#             }
#
#response = requests.request("POST", url, data=payload, headers=headers)
#
#res=response.text
#unittest.main()



# import unittest #自带单元测试的框架
# #  使用unittest中unittest.TestCase这个类
# #  可以对自动化测试用例进行管理，支持测试套件等
# #  所有的测试用力的函数必须以text开头，否则不认为写的代码是测试
# #  将test后面的字符串按照ASCII码进行排序，从上到下进行测试
# class qwe(unittest.TestCase):
#     def test_1(self):
#         a=4+5
#         print(123)
#         self.assertEqual(a,9)
#
#     def test_2(self):
#         b=9-6
#         print(456)
#         self.assertEqual(b,3)
#      #执行每一个测试用例前都要执行一次
#      # 初始化测试环境，保证任何一个用例都在同一个用例下执行
#     def setUp(self):
#         print('开始')
#     #执行每一个测试用例后都要执行一次
#     #清理测试环境，每一个测试用例执行完毕，将结果清楚掉，回到最开始的测试环境
#     def tearDown(self):
#         print('结束')
#
# if __name__=='__main__':  #统一执行测试，测试的函数必须以test开头
#     unittest.main()

# import requests
# import unittest
# import json
#
# class wind(unittest.TestCase):
#     def denglu(self,user,passwd):
#         url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
#
#         payload = '{"phone":"%s","password":"%s","zone":"86","loginType":0,"isAuto":0,"deviceId":"ec:89:14:54:93:007"}'%(user,passwd)
#         headers = {
#             'Content-Type': "application/json",
#             'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
#             'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
#             'Language': "zh_CN",
#             'APIVersion': "3.0",
#             'cache-control': "no-cache",
#             'Postman-Token': "c1b0547a-8ee5-434b-a79c-bbe40861fcd7"
#             }
#
#         response = requests.request("POST", url, data=payload, headers=headers)
#
#
#
#     def test_1(self):
#         qq=self.denglu(15993835273,111111)
#         self.assertEqual(qq['code'],0)
#     def test_2(self):
#         ww=self.denglu(15993835273,11111)
#         self.assertNotEqual(ww['code'],0)
# # if __name__ == '__main__':
# unittest.main()





import requests
import unittest#单元测试框架，编写测试用例，进行断言
import xlrd
import HTMLTestRunner
  #测试报告

def shuju():
    shuj=[]
    f=xlrd.open_workbook(r'b.xls')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        shuj.append(sheet.row_values(i))
    print(shuj)
    return shuj
shuju()

class wind(unittest.TestCase):
    aa=shuju()
    print(aa)
    def denglu(self,user,passwd):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"

        payload = '{"phone":"%s","password":"%s","zone":"86","loginType":0,"isAuto":0,"deviceId":"ec:89:14:54:93:007"}'%(user,passwd)
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
        res=response.json()
        return res

    def test_1(self):
        qq=self.denglu(int(self.aa[0][0]),int(self.aa[0][1]))
        self.assertEqual(qq['code'],0)
    def test_2(self):
        for j in range(2,3):
            ww=self.denglu(int(self.aa[j][0]),int(self.aa[j][1]))
            self.assertNotEqual(ww['code'],0)
if __name__ == '__main__':
    # unittest.main()  #测试报告不需要
    # 创建一个测试报告
    suit=unittest.TestSuite()

      #第一种方法 将测试用例添加到测试套件中
    # suit.addTest(wind('test_1'))  #wind为类名，括号在加引号的是函数名
    # suit.addTest(wind('test_2'))
      #第二种方法  #括号中为类名，是将wind类中的所有以test开头的函数都添加到测试套件中
    suit.addTest(unittest.makeSuite(wind))
    #打开一个空文件,必须为HTML后缀名
    f=open('abc.html','wb')
    #定义测试报告的信息
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='接口测试报告',tester='王玉鑫',description='结果如下:')
    #执行测试套件
    runner.run(suit)
    #关闭文件
    f.close()



