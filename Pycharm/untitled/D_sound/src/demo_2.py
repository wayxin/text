# -*- coding: utf-8 -*- 

# @Time : 2019/5/13 上午11:50 

# @Author : 废柴 

# @Project: D_sound

# @FileName : demo_2.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

from time import sleep
import unittest
from appium import webdriver


# class ce(unittest.TestCase):
#     a = {
#         "device": "android",
#         "platformName": "Android",
#         "platformVersion": "6.0.1",
#         "deviceName": "3493f5137d5",
#         "appPackage": "com.qk.butterfly",
#         "appActivity": ".main.LauncherActivity",
#         "noReset": "True"
#     }
#
#
#     dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
#     sleep(10)
#
#     def logout(self):
#         # find_element_by_class_name()  定位一个class属性的元素，要求该元素唯一
#         # find_elements_by_class_name()  定位多个class属性的元素，元素是多个
#         a = self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
#         print(a)
#
#
#
#
# if __name__ == '__main__':
#     go = ce()
#     go.logout()


a = {
    "device": "android",
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "3493f5137d5",
    "appPackage": "com.qk.butterfly",
    "appActivity": ".main.LauncherActivity",
    "noReset": "True"
}


dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
sleep(10)
dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
sleep(0.5)

dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('18538097372')
# 清空数据
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()



dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('18538097372')

#
#
#
# dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('dsound123456')
# sleep(5)
# a = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# print(a)
# a[-1].click()
#
# # 获取当前屏幕的分辨率
# size = dr.get_window_size()
#
# x1 = size['width'] * 0.5  # x坐标 50
# y1 = size['height'] * 0.25  # 起始y坐标 50
# y2 = size['height'] * 0.75  # 150
#
#
# for i in range(2):
#     dr.swipe(x1, y2, x1, y1)
#
# dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
# sleep(0.5)
# dr.find_element_by_id('com.qk.butterfly:id/v_me_grade').click()
# dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
#
# # 关闭app
# dr.quit()






