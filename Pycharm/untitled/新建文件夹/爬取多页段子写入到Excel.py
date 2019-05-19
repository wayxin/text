#! /usr/bin/python
# -*- coding:utf-8 -*-
# import requests
# import re
# ff=[]
# dd=[]
# for k in range(1,3):
#     a='http://www.qiushibaike.com/text/page/{}/.'.format(k)
#     #发送请求
#     oo={'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#     b=requests.get(a,headers=oo)
#     #接收响应
#     c=b.content.decode('utf-8')
#     z=re.compile('<h2>(.*?)</h2>',re.S)
#     v=z.findall(c)
#     d=re.compile('<div class="content">(.*?)</span>',re.S)
#     e=d.findall(c)
#     for j in v:
#         dd.append(j)
#     for i in e:
#         i=i.replace('<span>','')
#         i=i.strip()
#         i=i.replace('<br/>','')
#         ff.append(i)
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('qiushi')
# for x in range(len(dd)):
#     sheet.write(x,0,dd[x]+':')
#     sheet.write(x,1,ff[x])
# f.save('h.xls')