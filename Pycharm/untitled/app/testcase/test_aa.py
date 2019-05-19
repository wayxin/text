#! /usr/bin/python
#- -*- coding:utf-8 -*-
#导入函数
from app.func.duw import aa,bb,cc,dd
from appium import webdriver
from time import sleep
import unittest
import HTMLTestRunner
from app.ewwn import REPORT_DIR
from app.testcase.rizhi_mokuai import get_log

g=go=get_log(name='test_aa.py')
class ceshi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        d = {
                  "device": "android",
                  "platformName": "Android",
                  "platformVersion": "8.1.0",
                  "deviceName": "b13249e2",
                  "appPackage": "com.qk.butterfly",
                  "appActivity": ".main.LauncherActivity",
                  "noReset":"True"
            }
        g.info('连接建立成功')
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
        sleep(10.0)

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
    #测试用例的代码
    def test_1(self):
        #验证微信的用例
        text=aa(self.dr)
        self.assertEqual(text,'微信')
    def test_2(self):
        text=bb(self.dr)
        self.assertEqual(text,'微博')
    def test_3(self):
        text=cc(self.dr)
        self.assertEqual(text,'QQ')
    def test_4(self):
        text=dd(self.dr)
        self.assertEqual(text,'密码')
    g.info('测试完成')

if __name__ == '__main__':
    suit=unittest.TestSuite()
    suit.addTest(ceshi('test_1'))  #wind为类名，括号在加引号的是函数名
    suit.addTest(ceshi('test_2'))
      #第二种方法  #括号中为类名，是将wind类中的所有以test开头的函数都添加到测试套件中
    # suit.addTest(unittest.makeSuite(ceshi))
    re=REPORT_DIR+'HTMLReport.html'
    f=open(re,'wb')                                                            #verbosity默认是0,为2 可以使控制台输出的信息更加详细
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='接口测试报告',tester='王玉鑫',description='结果如下:')
    runner.run(suit)
    #关闭文件
    # f.close()


