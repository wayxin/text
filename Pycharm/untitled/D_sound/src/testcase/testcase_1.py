# -*- coding: utf-8 -*- 

# @Time : 2019/4/29 下午2:29 

# @Author : 废柴 

# @Project: D_sound

# @FileName : testcase_1.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================
from src.func.func_1 import item_data, check_text
from appium import webdriver
import unittest
from HTMLTestReportCN import HTMLTestRunner
from src.until.Myloger import get_logger
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions as ec
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

capabilities = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": "3493f5137d5",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }

# 日志模块

class TestCase(unittest.TestCase):

    def setUpClass(cls):
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
        element = (By.ID, 'com.qk.butterfly:id/tv_to_login')
        try:
            WebDriverWait(cls.dr, 10, 0.2).until(EC.presence_of_element_located(element))
        except ec.TimeoutException:
            print("元素未找到")

    def tearDownClass(cls):
        cls.dr.quit()

    def test_1(self):
        check_text(self.dr, 'wx_id', '微信')

    def test_2(self):
        check_text(self.dr, 'wb_id', '微博')
        
    def test_3(self):
        check_text(self.dr, 'qq_id', 'qq')
    
    def test_4(self):
        check_text(self.dr, 'pd_id', '密码')
    
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCase('test_1'))
    suite.addTest(TestCase('test_2'))
    suite.addTest(TestCase('test_3'))
    suite.addTest(TestCase('test_4'))
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase('test_1'))
    with open('HTMLReport.html', 'wb') as fb:
        runner = HTMLTestRunner(stream=fb,
                                title='测试报告',
                                description='报告的描述信息',
                                verbosity=2)
        runner.run(suite)
    


