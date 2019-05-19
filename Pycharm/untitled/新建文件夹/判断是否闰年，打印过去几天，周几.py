#! /usr/bin/python
# -*- coding:utf-8 -*-
# import time
# a=input("请输入日期:")
# b=a.split(',')
# c=[]
# for i in b:
#     c.append(int(i))
# if c[0]%400==0 or c[0]%4==0:
#     print('闰年')
# else:
#     print('非闰年')
# d=time.strptime('{},{},{}'.format(c[0],c[1],c[2]),'%Y,%m,%d')
# print('本年已经过去{}天,周{}'.format(d[-2],d[-3]+1))