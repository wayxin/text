#! /usr/bin/python
# -*- coding:utf-8 -*-
# a=[]
# b=input('请输入数字:')
# c=b.split(',')
# for i in c:
#     a.append(int(i))
# for x in range(1,len(a)):
#    for y in range(0,len(a)-1):
#        if a[y] > a[y+1]:
#            a[y],a[y+1]=a[y+1],a[y]
# print('最大值为{},第二大值为{}'.format(a[-1],a[-2]))
#升级版
# a = [1,4,3,2,4,5,5,7,6,7,5,7,6]
# c = []
# for i in a:
#     if i not in c:
#         c.append(i)
# for j in range(len(c)):
#     for x in range(len(c)-1):
#         if c[x] > c[x+1]:
#             c[x], c[x + 1] = c[x + 1], c[x]
# print(a.count(max(c)), '个', max(c))
# print(a.count(c[-2]), '个', c[-2])