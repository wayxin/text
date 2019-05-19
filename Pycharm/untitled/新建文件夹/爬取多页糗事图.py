#! /usr/bin/python
# -*- coding:utf-8 -*-
# import requests
# import re
# class tupian(object):
#     def fasongqingqiu(self,page):
#         url='https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
#         head={'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#         res=requests.get(url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         lianjie=[]
#         # ming=[]
#         patt=re.compile(r'<div class="thumb">(.*?)</a>',re.S)
#         items=patt.findall(abc)
#         # print(len(items))
#         for i in items:
#             new=re.compile(r'src="(.*?)"')
#             aaa=new.findall(i)
#             lianjie.append(aaa[0])
#         # kk=re.compile(r'<img width="100" alt="(.*?)" src="',re.S)
#         # name=kk.findall(abc)
#         # for j in name:
#         #     ming.append(j)
#         return lianjie
#     def save(self,shuju):
#         #需要请求图片的链接
#         global aa
#         for a,i in enumerate(shuju):
#             res=requests.get('https:'+i)
#             #注：接收响应的结果只能用content，因为图片是二进制
#             qq = res.content
#             with open('{}.jpg'.format(aa),'ab') as f:
#                 f.write(qq)
#             aa=aa+1
# tu=tupian()
# aa = 0
# for  ll in range(6):
#     ab=tu.fasongqingqiu(1)
#     tu.guolv(ab)
#     shu=tu.guolv(ab)
#     tu.save(shu)