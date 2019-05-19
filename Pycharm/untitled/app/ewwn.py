#! /usr/bin/python
#- -*- coding:utf-8 -*-
import os
#显示当前文件的绝对路径
a=os.path.dirname(os.path.abspath(__file__))
print(a)
#日志目录
LOG_DIR=a+'/logs/'
#报告目录
REPORT_DIR=a+'/report/'
#源文件目录
SRC_CASE=a+'/app/'
#测试用例目录
TEST_CASE=a+'/testcase/'
#页面方法目录
FUNC=a+'/func/'
#公共目录
UNTIL=a+'/until/'
