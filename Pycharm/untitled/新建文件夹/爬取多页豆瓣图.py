#! /usr/bin/python
# -*- coding:utf-8 -*-
# import requests
# import re
# class tupian(object):
#     def fasongqingqiu(self,page):
#         url='https://movie.douban.com/top250?start={}&filter='.format(page)
#         head={'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#         res=requests.get(url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         lianjie=[]
#         ming=[]
#         patt=re.compile(r'<img width="100" (.*?)</a>',re.S)
#         items=patt.findall(abc)
#         # print(len(items))
#         for i in items:
#             new=re.compile(r'src="(.*?)"')
#             aaa=new.findall(i)
#             lianjie.append(aaa[0])
#         kk=re.compile(r'<img width="100" alt="(.*?)" src="',re.S)
#         name=kk.findall(abc)
#         for j in name:
#             ming.append(j)
#         return lianjie,ming
#     def save(self,shuju,mingzi):
#         #需要请求图片的链接
#         for a,i in enumerate(shuju):
#             res=requests.get(i)
#             #注：接收响应的结果只能用content，因为图片是二进制
#             qq = res.content
#             z=mingzi[a]
#             with open('{}.jpg'.format(z),'ab') as f:
#                 f.write(qq)

# tu=tupian()
# for  ll in range(0,125,25):
#     ab=tu.fasongqingqiu(ll)
#     tu.guolv(ab)
#     shu,m=tu.guolv(ab)
#     tu.save(shu,m)
