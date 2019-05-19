# -*- coding: utf-8 -*- 

# @Time : 2019/5/13 下午5:16 

# @Author : 废柴 

# @Project: D_sound

# @FileName : func_2.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================
import yaml
from appium import webdriver


# 建立连接的参数
a = {
    "device": "android",
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "3493f5137d5",
    "appPackage": "com.qk.butterfly",
    "appActivity": ".main.LauncherActivity",
    "noReset": "True"
}
#  app建立连接
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=a)


with open('/Users/oldman/D_sound/src/element/a.yaml', 'r', encoding='utf-8') as fb:
    # a = yaml.load(fb)  使用yaml模块的load方法将yaml文件中的数据转换成python字典的形式
    item_data = yaml.load(fb)  # 字典
print(item_data)
print(type(item_data))
print(item_data['three']['wx_id'])

def foo(driver):
    # dr = driver
    text = driver.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name(
        'android.widget.TextView').text
    #   weixin
    return text





