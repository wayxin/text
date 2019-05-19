#! /usr/bin/python
# -*- coding:utf-8 -*-
# 将爬取的内容添加到数据库
# import pymysql
# # # 连接数据库
# conn=pymysql.connect(host='192.168.2.115',port=3306,user='root',passwd='123456')
#
# mycusor=conn.cursor()
# import requests
# # #创建游标:conn.cursor
# import re
# class boss():
#     def qingqiu(self,page=1):
#         url=url='https://www.zhipin.com/c101280100/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&page={1}&ka=page-{1}'
#         head = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#         res = requests.get(url, headers=head)
#         html = res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         gongsi0=[]
#         dizhi0=[]
#         jingyan0=[]
#         xueli0=[]
#         shangshi0=[]
#         lv1=re.compile(r'<div class="job-title">(.*?)</div>',re.S)
#         zhiwei=lv1.findall(abc)
#         lv2=re.compile(r'<span class="red">(.*?)</span>',re.S)
#         xinzi=lv2.findall(abc)
#         lv3=re.compile(r'<div class="company-text">(.*?)</h3>',re.S)
#         g=lv3.findall(abc)
#         for i in g:
#             lv31=re.compile(r'blank">(.*?)</a>',re.S)
#             gongsi=lv31.findall(i)
#             gongsi0.append(gongsi[0])
#         # lv6=re.compile(r'<div class="company-text">(.*?)</p>',re.S)
#         # shangshi1=lv6.findall(abc)
#         # for p in shangshi1:
#         #     lv32 = re.compile(r'<em class="vline"></em>(.*?<em class="vline">)', re.S)
#         #     shangshi = lv32.findall(p)
#
#         lv4=re.compile(r' <div class="info-detail"></div>(.*?)/p>',re.S)
#         dizhi=lv4.findall(abc)
#
#         for j in dizhi:
#             lv41=re.compile(r'<p>(.*?)<em class="vline">',re.S)
#             dizhi1=lv41.findall(j)
#             dizhi0.append(dizhi1[0])
#             lv42=re.compile(r'</em>(.*?)<em',re.S)
#             jingyan=lv42.findall(j)
#             jingyan0.append(jingyan[0])
#             lv43=re.compile(r'(大专|本科|学历不限|硕士|中专/中技|高中)',re.S)
#             xueli=lv43.findall(j)
#             xueli0.append(xueli[0])
#         return list(zip(zhiwei,xinzi,dizhi0,jingyan0,xueli0,gongsi0))
# b=boss()
# f=b.qingqiu()
# tt=b.guolv(f)
# # print(tt)
#
# mycusor=conn.cursor()
# mycusor.execute('use li_text')
# for q,w,e,r,t,y in tt:
#     mycusor.execute('insert into boss values("{}","{}","{}","{}","{}","{}")'.format(q,w,e,r,t,y))
#     conn.commit()