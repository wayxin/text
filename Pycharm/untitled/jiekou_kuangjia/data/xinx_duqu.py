#! /usr/bin/python
#- -*- coding:utf-8 -*-
import xlrd
def xx():
    xinx=[]
    f=xlrd.open_workbook(r'H:\PycharmProjects\untitled\jiekou_kuangjia\data\AA.xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        xinx.append(sheet.row_values(i))
    # print(xinx)
    return xinx
xx()