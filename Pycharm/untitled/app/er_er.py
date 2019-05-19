#! /usr/bin/python
# #- -*- coding:utf-8 -*-
# from appium import webdriver
# from time import sleep
# import unittest
#
# #连接测试脚本与appium服务器进行连接的参数数据
# class DS(unittest.TestCase):
#     d={
#         "device": "android",
#         "platformName": "Android",
#         "platformVersion": "8.1.0",
#         "deviceName": "b13249e2",
#         "appPackage": "com.qk.butterfly",
#         "appActivity": ".main.LauncherActivity",
#         "noReset": "True"
#     }
# #
#     #初始化环境
#     # def setUp(self):
#     #     self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
#     #     sleep(10.0)
#     # def __init__(self):
#     #     self.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.d)
#         # 所有的用例执行之前，跑一次，只跑一次
#     @classmethod
#     def setUpClass(cls):
#         cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.d)
#         sleep(10.0)
#
#         # 所有的用例执行之后，跑一次，只跑一次
#     @classmethod
#     def tearDownClass(cls):
#         cls.dr.quit()
#
#
# #测试写断言
#     def test_1(self):
#         wenben_1 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
#         self.assertEqual(wenben_1,'微信')
#         wenben_2 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
#         self.assertEqual(wenben_2,'微博')
#     def test_2(self):
#         wenben_3=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
#         self.assertEqual(wenben_3,'QQ')
#         wenben_4=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
#         self.assertEqual(wenben_4,'密码')
#
#     # def tearDown(self):
#     #     self.dr.quit()
#
#     #检查微信，QQ，微博等的函数/方法
#     # def wenben(self):
#     #     #获取微信文字
#     #     wenben_1 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
#     #     wenben_2=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
#     #     wenben_3=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
#     #     wenben_4=self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
#     #     print(wenben_1,wenben_2,wenben_3,wenben_4)
#     #     return wenben_1,wenben_2,wenben_3,wenben_4
#     #关闭APP并退出
#     # def guanbi(self):
#     #     self.dr.quit()
#
# if __name__=='__main__':
#     unittest.main()
#     #verbosity=2,warnings=True
#     go=DS()   #创建一个DS类的实例，赋值给变量go
#     # sleep(10.0)
#     # go.wenben()
#     # go.guanbi()






















from appium import webdriver
from time import sleep

#连接测试脚本与appium服务器进行连接的参数数据
class DS(object):
    d={
        "device": "android",
        "platformName": "Android",
        "platformVersion": "8.1.0",
        "deviceName": "b13249e2",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }

#     def __init__(self):
#         self.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.d)
#         sleep(5.0)
#     def tiao_zhuan(self):
#         self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
#
#     #账号密码输入参数
#     def login(self,phone,password):
#         # aa = shuju()
#         # 向账号输入框内输入手机号
#         self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)
#         #向密码输入框内输入手机号
#         self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
#         #点击登录按钮
#         self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
#         sleep(5.0)
#     def guanbi(self):
#         self.dr.quit()
#
if __name__ == '__main__':
    # unittest.main()
    #创建一个DS类的实例，赋值给变量go
    go=DS()
    #跳转DS类的方法，跳转页面
    # go.tiao_zhuan()
    # #输入手机号，密码，执行登录
    # go.login('17630926181','woshengri0902')
    # #关闭手机APP并退出
    # go.guanbi()