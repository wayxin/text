#! /usr/bin/python
# -*- coding:utf-8 -*-
def yinshu(a):
    c=0
    for i in range(1,a+1):
        b = 0
        for j in range(1,i):
            if i%j==0:
                c=c+j
        if c==i:
            print(i)
            # c=c+i

yinshu(100)
