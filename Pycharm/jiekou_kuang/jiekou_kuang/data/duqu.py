#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd

class Shuju():
	def shuju(self):
		shuj = []
		f = xlrd.open_workbook(r'C:\Users\join\Desktop\python_dome\jiekou_kuang\data\aa.xls')
		sheet = f.sheets()[0]
		for i in range(sheet.nrows):
			shuj.append(sheet.row_values(i))
		return shuj
