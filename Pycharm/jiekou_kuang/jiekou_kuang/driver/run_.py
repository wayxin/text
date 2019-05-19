#!/usr/bin/python
#-*- coding:utf-8 -*-

from jiekou_kuang.report.baogao import Baogao
with open('a.txt','r') as f:
    bb = f.readlines()

if 'all' in bb:
    Baogao('*')
else:
    Baogao(bb)