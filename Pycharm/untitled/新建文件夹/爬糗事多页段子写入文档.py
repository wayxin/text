#! /usr/bin/python
# -*- coding:utf-8 -*-
# import requests
# import re
# for k in range(1,6):
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
#     ff=[]
#     for i in e:
#         i=i.replace('<span>','')
#         i=i.strip()
#         i=i.replace('<br/>','')
#         ff.append(i)
#     with open('h.txt','a',encoding='utf-8') as j:
#                 for i in ff:
#                     s=ff.index(i)
#                     j.write(v[s])
#                     j.write(i)