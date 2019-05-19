#! /usr/bin/python
#- -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

class wangzhan(object):
    jd=webdriver.Firefox()
    jd.get('https://www.jd.com')
    sleep(2)
    def denglu(self):
        self.jd.maximize_window()
        sleep(2)
        self.jd.find_element_by_class_name('link-login').click()
        sleep(2)
        self.jd.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/a').click()
        sleep(2)
        self.jd.find_element_by_id('loginname').send_keys('17630926181')
        sleep(2)
        self.jd.find_element_by_id('nloginpwd').send_keys('woshengri0902')
        sleep(2)
        self.jd.find_element_by_id('loginsubmit').click()
        sleep(10)
    def chazhao(self):
        self.jd.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[1]/div/ul/li[6]/a[1]').click()
        sleep(2)
        aa_1 = self.jd.window_handles
        self.jd.switch_to_window(aa_1[-1])
        print(aa_1)
        sleep(5)
        self.jd.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/a[2]').click()
        sleep(2)
        aa_2=self.jd.window_handles
        self.jd.switch_to_window(aa_2[-1])
        print(aa_2)
        self.jd.find_element_by_xpath('/html/body/div[8]/div[1]/div[1]/div[3]/div/div[2]/div[1]/ul/li[2]/a').click()
        sleep(2)
    def tianjia_gwc(self):
        self.jd.find_element_by_xpath('/html/body/div[8]/div[1]/div[3]/div[1]/div/div[3]/ul/li[3]/div/div[1]/a/img').click()
        sleep(2)
        aa_3 = self.jd.window_handles
        self.jd.switch_to_window(aa_3[-1])
        print(aa_3)
        self.jd.find_element_by_id('InitCartUrl').click()
        sleep(2)

jj=wangzhan()
jj.denglu()
jj.chazhao()
jj.tianjia_gwc()