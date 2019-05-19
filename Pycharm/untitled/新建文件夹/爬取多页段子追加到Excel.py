#! /usr/bin/python
# -*- coding:utf-8 -*-
# import xlwt
# import xlrd
# from xlutils.copy import copy
# import requests
# import re
# for k in range(1,5):
#     a = 'http://www.qiushibaike.com/text/page/{}/.'.format(k)
#     # 发送请求
#     oo = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#     b = requests.get(a, headers=oo)
#     # 接收响应
#     c = b.content.decode('utf-8')
#     z = re.compile('<h2>(.*?)</h2>', re.S)
#     v = z.findall(c)
#     d = re.compile('<div class="content">(.*?)</span>', re.S)
#     e = d.findall(c)
#     ff = []
#     for i in e:
#         i = i.replace('<span>', '')
#         i = i.strip()
#         i = i.replace('<br/>', '')
#         ff.append(i)
#     try:
#         fff = xlrd.open_workbook('h.xls')
#         sheet1=fff.sheets()[0]
#         num=sheet1.nrows
#         print(num)
#         new_f=copy(fff)
#         sheet=new_f.get_sheet(0)
#         for i,j in enumerate(ff):
#             sheet.write(num+i,0,v[i]+':')
#             sheet.write(num+i,1,j)
#         new_f.save('h.xls')
#     except:
#         f = xlwt.Workbook()
#         sheet = f.add_sheet('qiushi')
#         l = 0
#         for y in v:
#             sheet.write(l, 0, y + ':')
#             l = l + 1
#         p = 0
#         for j in ff:
#             sheet.write(p, 1, j)
#             p = p + 1
#         f.save('h.xls')