# -*- coding: utf-8 -*- 

# @Time : 2019/5/11 下午2:27 

# @Author : 废柴 

# @Project: D_sound

# @FileName : demo_1.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

第一步导入appium模块中的webdriver类
from appium import webdriver
from time import sleep

面向过程

测试脚本与appium服务器进行连接的参数数据

d = {
    "device": "android",
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "3493f5137d5",
    "appPackage": "com.qk.butterfly",
    "appActivity": ".main.LauncherActivity",
    "noReset": "True"
}

# 写死的 http://127.0.0.1:4723/wd/hub
# 测试脚本是appium服务器与手机建立连接的过程

dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
# sleep(10.0)

# 元素是id，就使用id定位方法
dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').click()

# 获取微信的文字
# 元素的多级定位。
# 先定位上一级，再定位下面的元素。没有id，找class属性。
text = dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# print(text)

# 插入等待时间,休眠几秒
# sleep(2.0)


# send_keys() 输入的是字符串
#  什么时候可以用send_keys？
# 1 向手机的输入框内输入的数据的时候
# 2 clickable ---》true
# 3 enabled ---》 true
# 4 foucsable --》 true

# 向账号输入框内输入手机号
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('15638292964')
# 向密码输入框内输入密码


# dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('密码')

# 查看登录后的效果
# sleep(10)

# 退出app，包括后台进程也关掉
# dr.quit()

# ######################## 面向对象 ###################


# from appium import webdriver
# from time import sleep
#
#
# class DS(object):
#
#     # 测试脚本与appium服务器进行连接的参数数据
#     d = {
#         "device": "android",
#         "platformName": "Android",
#         "platformVersion": "6.0.1",
#         "deviceName": "3493f5137d5",
#         "appPackage": "com.qk.butterfly",
#         "appActivity": ".main.LauncherActivity",
#         "noReset": "True"
#     }
#
#     # 建立连接的函数
#     def __init__(self):
#
#         self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
#         sleep(10.0)
#
#     # 检查那四个文字的函数/方法
#     def check_text(self):
#
#         # 获取微信文字
#         text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
#         print(text)
#         return text
#
#     # 关闭app的函数
#     def close_app(self):
#         self.dr.quit()
#
#
# if __name__ == '__main__':
#     go = DS()  # 创建一个DS类的实例，赋值给变量go
#     # 调用DS类的方法
#     go.check_text()
#     go.close_app()

# from appium import webdriver
# from time import sleep
# import unittest
# import warnings
# warnings.simplefilter('ignore',ResourceWarning)
#
#
# class DS(unittest.TestCase):
#
#     # 测试脚本与appium服务器进行连接的参数数据
#     d = {
#         "device": "android",
#         "platformName": "Android",
#         "platformVersion": "6.0.1",
#         "deviceName": "3493f5137d5",
#         "appPackage": "com.qk.butterfly",
#         "appActivity": ".main.LauncherActivity",
#         "noReset": "True"
#     }
#
#     # # 初始化测试环境的方法/函数
#     # def setUp(self):
#     #     self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
#     #     sleep(10.0)
#
#     # 所有的用例执行之前，跑一次，就跑一次
#     @classmethod
#     def setUpClass(cls):
#         cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.d)
#         sleep(10.0)
#
#     # 所有的用例执行完毕，跑一次，就跑一次  # @classmethod  固定写法
#     @classmethod
#     def tearDownClass(cls):
#         cls.dr.quit()
#
#     # 断言微信文字是否存在
#     def test_1(self):
#
#         text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
#         print(text)
#         # 断言
#         self.assertEqual(text, '微信')
#
#
#     # # 清理测试环境
#     # def tearDown(self):
#     #     self.dr.quit()
#
#
# if __name__ == '__main__':
#     """
#     verbosity=2,
#     使输出信息更详细
#
#     """
#     unittest.main(verbosity=2)




# 测试手机输入框
from appium import webdriver
from time import sleep


class DS(object):

    # 测试脚本与appium服务器进行连接的参数数据
    d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": "3493f5137d5",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }

    # 建立连接的函数
    def __init__(self):

        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
        sleep(10.0)

    # 跳转至手机号/密
    # 码登录页面的函数
    def tiao_zhuan(self):
        # 点击密码图标
        self.dr.find_element_by_id('xxxx').click()
        sleep(2)

    # 账号密码输入函数
    def login(self, phone, password):

        # 向账号输入框内输入手机号
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)
        # 向密码输入框内输入密码
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
        # 点击登录按钮
        self.dr.find_element_by_id('').click()
        # 查看登录之后的效果
        sleep(5)

    # 关闭app的函数
    def close_app(self):
        self.dr.quit()


if __name__ == '__main__':
    go = DS()  # 创建一个DS类的实例，赋值给变量go == self cls
    # 调用DS类的方法
    # 跳转页面
    go.tiao_zhuan()
    # 执行登录
    go.login('15638292964','xxx')
    # 关闭手机app
    go.close_app()





















