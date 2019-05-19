#! /usr/bin/python
#- -*- coding:utf-8 -*-
#1.下载模块  selenium
from selenium import webdriver
dr=webdriver.Firefox()

dr.get('https://www.baidu.com')