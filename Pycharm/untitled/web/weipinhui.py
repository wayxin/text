#! /usr/bin/python
#- -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
class weipinhui(object):
    wph=webdriver.Firefox()
    wph.get('https://www.vip.com/')
    sleep(5)
    def denglu(self):
        self.wph.find_element_by_xpath('/html/body/header/nav[1]/div/ul/li[1]/ul/li[1]/span[2]/a').click()
        sleep(2)
        self.wph.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[1]/div[2]').click()
        sleep(2)
        self.wph.find_element_by_id('J_login_name').send_keys('17630926181')
        sleep(2)
        self.wph.find_element_by_id('J_login_pwd').send_keys('woshengri0902')
        sleep(2)
        self.wph.find_element_by_id('J_login_submit').click()
        sleep(2)

vip=weipinhui()
vip.denglu()