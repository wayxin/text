#! /usr/bin/python
#- -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep


a={
  "device": "android",
  "platformName": "Android",
  "platformVersion": "8.1.0",
  "deviceName": "b13249e2",
  "appPackage": "com.wayyue.shanzhen",
  "appActivity": ".view.main.SZMainActivity",
  "noReset": "True"
}
dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=a)
sleep(5.0)

geren=dr.find_elements_by_class_name('android.widget.LinearLayout')
print(geren)
sleep(2.0)
geren[5].click()
# sleep(5.0)
# geren[6]
# sleep(2.0)