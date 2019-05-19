#! /usr/bin/python
# -*- coding:utf-8 -*-
# a=input('请输入数据:')
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# c=[]
# for i in b:
#     c.append(int(i))
# for x in range(1,len(c)):
#     for y in range(0,len(c)-1):
#         if c[y]>c[y+1]:
#             c[y],c[y+1]=c[y+1],c[y]
# print(c)




def qc(aa):
    b=[]
    c=[]
    d=aa.split(',')
    for i in d:
        b.append(int(i))
        for j in b:
            if j not in c:
                c.append(j)
    for x in range(1,len(c)):
        for y in range(0,len(c)-1):
            if c[y]>c[y+1]:
                c[y],c[y+1]=c[y+1],c[y]
    print(c)
qc('12,32,9,18,9,12,98,18')




