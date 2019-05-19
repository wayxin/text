# -*- coding: utf-8 -*- 

# @Time : 2019/5/13 下午5:33 

# @Author : 废柴 

# @Project: D_sound

# @FileName : testcase_2.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

# # 导入函数

from src.func.func_2 import foo
from appium import webdriver


# 建立连接
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
foo(dr)

