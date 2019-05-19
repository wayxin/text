# -*- coding: utf-8 -*- 

# @Time : 2019/4/27 下午4:04 

# @Author : 废柴 

# @Project: D_sound

# @FileName : demo.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================
import yaml
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions as ec
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# def element(var):
#     """
#     读取定位元素文件方法---加载ElementPage目录下的各个马甲包文件定位文件名
#     :param var: 定位元素文件名
#     :return: 定位元素文件的全部数据
#     """
#     # with open(var, 'r') as fb:
#     #     temp = yaml.load(fb)
#     # return temp
#     with open(var, 'r', encoding='utf-8') as fb:
#         return yaml.load(fb)

with open('/Users/oldman/D_sound/item.yaml', 'r', encoding='utf-8') as fb:
    item_data = yaml.load(fb)

# 设备信息
capabilities = {
    "device": "android",
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "3493f5137d5",
    "appPackage": "com.qk.butterfly",
    "appActivity": ".main.LauncherActivity",
    "noReset": "True"
}
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)

# 等待某个元素
# element = (By.ID, 'com.qk.butterfly:id/tv_to_login')
element = (By.ID, 'com.qk.butterfly:id/tv_cancel')
try:
    WebDriverWait(dr, 10, 0.2).until(EC.presence_of_element_located(element))
except ec.TimeoutException:
    print("目标元素未找到")

# # 获取第三方文本
# text = dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# print(text)
# dr.quit()

# 进入到账号密码登录页面
# dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
# sleep(0.5)
# 输入账号
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('18538097372')
# 输入密码

dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('dsound123456')
# 点击登录按钮进行登录
# dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
# sleep(5)
# 登录之后进行断言

dr.find_element_by_id('com.qk.butterfly:id/tv_cancel').click()
nav = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
for i in nav:
    i.click()
    sleep(2.0)






# 获取当前屏幕的分辨率
size = dr.get_window_size()

x1 = size['width'] * 0.5  # x坐标 50
y1 = size['height'] * 0.25  # 起始y坐标 50
y2 = size['height'] * 0.75  # 150


for i in range(2):
    dr.swipe(x1, y2, x1, y1)

dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
sleep(0.5)
dr.find_element_by_id('com.qk.butterfly:id/v_me_grade').click()
dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()

# 关闭app
dr.quit()


"""
def swipe_up(argument, t=500, n=2):
    # 向上滑动屏幕
    size = argument.get_window_size()
    x1 = size['width'] * 0.5  # x坐标 50
    y1 = size['height'] * 0.25  # 起始y坐标 50
    y2 = size['height'] * 0.75  # 150
    for i in range(n):
        argument.swipe(x1, y2, x1, y1, t)


def swipe_down(argument, t=500, n=2):
    # 向下滑动屏幕
    size = argument.get_window_size()
    x1 = size['width'] * 0.5  # x坐标
    y1 = size['height'] * 0.25  # 起始y坐标
    y2 = size['height'] * 0.75
    for i in range(n):
        argument.swipe(x1, y1, x1, y2, t)


def swipe_left(argument, t=500, n=2):
    # 向左滑动屏幕
    size = argument.get_window_size()
    x1 = size['width'] * 0.5  # x坐标
    x2 = size['width'] * 0.25  # 起始y坐标
    y1 = size['height'] * 0.75
    for i in range(n):
        argument.swipe(x1, y1, x2, y1, t)


def swipe_right(argument, t=500, n=2):
    # 向右滑动屏幕
    size = argument.get_window_size()
    x1 = size['width'] * 0.5  # x坐标
    x2 = size['height'] * 0.25  # 起始y坐标
    y1 = size['height'] * 0.75
    for i in range(n):
        argument.swipe(x2, y1, x1, y1, t)


"""