#! /usr/bin/python
#- -*- coding:utf-8 -*-
from time import sleep
import unittest
from appium import webdriver
class DY(unittest.TestCase):
    dd={
  "device": "android",
  "platformName": "Android",
  "platformVersion": "8.1.0",
  "deviceName": "b13249e2",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": ".main.MainActivity",
  "noReset": "True"
}
    dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=dd)
    sleep(10.0)
    def shang_hua(self):
        while True:
            sleep(3.0)
            size = self.dr.get_window_size()
            x1 = size['width'] * 0.5
            y1 = size['height'] * 0.25
            y2 = size['height'] * 0.75
            for i in range(2):
                self.dr.swipe(x1, y2, x1, y1)
                sleep(15.0)
    def tuichu(self):
        self.dr.quit()

if __name__ == '__main__':
    dy=DY()
    dy.shang_hua()
    dy.tuichu()