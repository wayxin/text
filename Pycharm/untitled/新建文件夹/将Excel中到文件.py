#! /usr/bin/python
# -*- coding:utf-8 -*-
# import  xlrd
# f=xlrd.open_workbook('a.xls')
# sheet=f.sheets()[0]
# c=sheet.nrows
# x=open('c.txt','w',encoding='utf-8')
# for i in range(c):
#     j=sheet.row_values(i)
#     for m,k in enumerate(j):
#         print(m,k)
#         if m==len(j)-1:
#             x.write(k)
#         else:
#             x.write(k+',')
# f.save('d.xls')