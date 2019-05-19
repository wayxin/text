#! /usr/bin/python
#- -*- coding:utf-8 -*-
import unittest
from app.testcase import HTMLTestRunner
from jiekou_kuangjia.ww_test.test_gexinxi import eren
suit = unittest.TestSuite()
suit.addTest(eren('test_one'))  #wind为类名，括号在加引号的是函数名
suit.addTest(eren('test_tuo'))
f = open('a.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='王玉鑫', description='结果如下:')
runner.run(suit)
f.close()