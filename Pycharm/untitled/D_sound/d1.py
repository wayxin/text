# -*- coding: utf-8 -*- 

# @Time : 2019/4/26 下午3:46 

# @Author : 废柴 

# @Project: D_sound

# @FileName : d1.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================
import unittest
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from HTMLTestReportCN import HTMLTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as ec
import yaml

# 读取定位元素的数据
with open('/Users/oldman/D_sound/item.yaml', 'r', encoding='utf-8') as fb:
    item_data = yaml.load(fb)
# print(item_data)


class D_Sound(unittest.TestCase):
    capabilities = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": "3493f5137d5",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }

    def setUp(self):
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.capabilities)
        # self.dr.implicitly_wait(10)   # 超时等待
        element = (By.ID, 'com.qk.butterfly:id/tv_to_login')
        try:
            WebDriverWait(self.dr, 10, 0.2).until(EC.presence_of_element_located(element))
        except ec.TimeoutException:
            print("元素未找到")

    def test_1(self):
        text = self.dr.find_element_by_id(item_data['three']['wx_id']).find_element_by_class_name\
            (item_data['ut']['TextView_classs']).text
        self.assertEqual(text, u'微信')

    def test_2(self):
        text = self.dr.find_element_by_id(item_data['three']['wb_id']).find_element_by_class_name \
            (item_data['ut']['TextView_classs']).text
        self.assertEqual(text, u'微bo')

    def test_3(self):
        text = self.dr.find_element_by_id(item_data['three']['qq_id']).find_element_by_class_name \
            (item_data['ut']['TextView_classs']).text
        self.assertEqual(text, u'qq')

    def test_4(self):
        text = self.dr.find_element_by_id(item_data['three']['pd_id']).find_element_by_class_name \
            (item_data['ut']['TextView_classs']).text
        self.assertEqual(text, u'密码')

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(D_Sound('test_1'))
    suite.addTest(D_Sound('test_2'))
    suite.addTest(D_Sound('test_3'))
    suite.addTest(D_Sound('test_4'))
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase('test_1'))
    with open('HTMLReport.html', 'wb') as fb:
        runner = HTMLTestRunner(stream=fb,
                                title='测试报告',
                                description='报告的描述信息',
                                verbosity=2)
        runner.run(suite)
    # unittest.main(warnings='ignore', verbosity=2)

capabilities = {
    "device": "android",
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "3493f5137d5",
    "appPackage": "com.qk.butterfly",
    "appActivity": ".main.LauncherActivity",
    "noReset": "True"
}



"""
selenium.webdriver.support.wait.WebDriverWait（类）

__init__
    driver: 传入WebDriver实例，即我们上例中的driver
    timeout: 超时时间，等待的最长时间（同时要考虑隐性等待时间）
    poll_frequency: 调用until或until_not中的方法的间隔时间，默认是0.5秒
    ignored_exceptions: 忽略的异常，如果在调用until或until_not的过程中抛出这个元组中的异常，
            则不中断代码，继续等待，如果抛出的是这个元组外的异常，则中断代码，抛出异常。默认只有NoSuchElementException。

until
    method: 在等待期间，每隔一段时间调用这个传入的方法，直到返回值不是False
    message: 如果超时，抛出TimeoutException，将message传入异常

until_not 与until相反，until是当某元素出现或什么条件成立则继续执行，
        until_not是当某元素消失或什么条件不成立则继续执行，参数也相同，不再赘述。
    method
    message
    
    
    selenium.webdriver.support.expected_conditions（模块）

这两个条件类验证title，验证传入的参数title是否等于或包含于driver.title
title_is
title_contains

这两个人条件验证元素是否出现，传入的参数都是元组类型的locator，如(By.ID, 'kw')
顾名思义，一个只要一个符合条件的元素加载出来就通过；另一个必须所有符合条件的元素都加载出来才行
presence_of_element_located
presence_of_all_elements_located

这三个条件验证元素是否可见，前两个传入参数是元组类型的locator，第三个传入WebElement
第一个和第三个其实质是一样的
visibility_of_element_located
invisibility_of_element_located
visibility_of

这两个人条件判断某段文本是否出现在某元素中，一个判断元素的text，一个判断元素的value
text_to_be_present_in_element
text_to_be_present_in_element_value

这个条件判断frame是否可切入，可传入locator元组或者直接传入定位方式：id、name、index或WebElement
frame_to_be_available_and_switch_to_it

这个条件判断是否有alert出现
alert_is_present

这个条件判断元素是否可点击，传入locator
element_to_be_clickable

这四个条件判断元素是否被选中，第一个条件传入WebElement对象，第二个传入locator元组
第三个传入WebElement对象以及状态，相等返回True，否则返回False
第四个传入locator以及状态，相等返回True，否则返回False
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be

最后一个条件判断一个元素是否仍在DOM中，传入WebElement对象，可以判断页面是否刷新了
staleness_of
"""
