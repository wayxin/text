#! /usr/bin/python
#- -*- coding:utf-8 -*-
from jiekou_kuangjia.report.baog import baogao

with open('a.txt','r')as f:
    qq=f.readlines()
if "all" in qq:
    print(qq[0])
    baogao('*')
else:
    baogao(qq)