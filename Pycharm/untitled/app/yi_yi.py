#! /usr/bin/python
#- -*- coding:utf-8 -*-
# 1.导入appium中的webdrive类
# from appium import webdriver
# from time import sleep
#
# #面向过程
# #测试脚本与appium服务器进行连接的参数数据
# d={
#   "device": "android",
#   "platformName": "Android",
#   "platformVersion": "8.1.0",
#   "deviceName": "b13249e2",
#   "appPackage": "com.qk.butterfly",
#   "appActivity": ".main.LauncherActivity",
#   "noReset": "True"
# }
# #将参数实例化,路径是写死的;测试脚本是appium服务器与手机建立连接的过程
# dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
#
# sleep(10.0)
# #元素为id，就使用id定位方法
# # dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').click()
# #元素的多级定位：先定位上一级，再定位下面的元素，没有id，找class属性
# #获取”微信“文本
# # wenben_1=dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# # wenben_2=dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
# # wenben_3=dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
# # wenben_4=dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
# # print(wenben_1,wenben_2,wenben_3,wenben_4)
# #
# # #插入等待时间,休眠三秒不执行代码
# # sleep(3.0)
# #send_keys()括号中输入的为字符串，是手机号
# #什么时候用send_keys()？
# #1.向手机的输入框输入数据的时候
# #2.clickable为true时
# #3.enable也为true时
# #4.foucsable也为true时
# dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
# dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('17630926181')
# dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('woshengri0902')
# dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
#
# #查看登录后的结果
# sleep(10.0)
# #退出APP，包括后台进程也关掉
# dr.quit()

from time import sleep
import unittest
from appium import webdriver

a = {
                  "device": "android",
                  "platformName": "Android",
                  "platformVersion": "8.1.0",
                  "deviceName": "b13249e2",
                  "appPackage": "com.qk.butterfly",
                  "appActivity": ".main.LauncherActivity",
                  "noReset":"True"
            }
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)
sleep(10)
dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('1763092618')
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()  #清空输入框中数据
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('1763092618')
dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('woshengri0902')
dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()


a = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
print(a)
a[3].click()
#获取当前屏幕的分辨率
size = dr.get_window_size()
x1=size['width']*0.5 #坐标50
y1=size['height']*0.25 #起始y坐标
y2=size['height']*0.75

for i in range(2):
  dr.swipe(x1,y2,x1,y1)

dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
dr.find_element_by_id('com.qk.butterfly:id/v_me_online').click()
dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()

dr.quit()
