


#爬虫步骤：
#1.分析网址   找到网址能够批量操作的规律
# import requests
# import re
# wangzhi='https://www.qiushibaike.com/text/page/{}/'.format(1)  #爬取网址的第一页
# #发送请求   依赖requests
# #反爬程序：  频繁访问会拉黑IP地址
# a={
# 'User-Agent':'Mozilla/5.0(Windows NT10.0;Win64;x64;rv:66.0)Gecko/20100101 Firefox/66.0'
# }
#
# b=requests.get(wangzhi,headers=a)
# #接受响应 1.text文本接受方式  （字符串 ）   2.content   (以字节的方式接受)
# # print(b.text)   #接受的是网页的源代码
# c=b.content.decode('utf-8')  #以b开头   要查看网页源代码中查看编码方式，
# #2.过滤想要的内容    用正则表达式
# d=re.compile('<div class="content">(.*?)</span>',re.S)
# f=d.findall(c)
# ff=[]
# for i in f:
#     i=i.replace('<span>','')
#     i = i.strip()
#     i=i.replace('<br/>','')
#     ff.append(i)
# with open('a.txt','w',encoding='utf-8')as g:
#     for i in ff:
#         g.write(i+'\n'+'\n')


# 将作者名称和段子放在表格中
# import requests
# import re
# import xlwt
# ff = []
# aa = []
# for k in range(1,6):
#     wangzhi='https://www.qiushibaike.com/text/page/{}/'.format(k)
#     a={
#     'User-Agent':'Mozilla/5.0(Windows NT10.0;Win64;x64;rv:66.0)Gecko/20100101 Firefox/66.0'
#     }
#     b=requests.get(wangzhi,headers=a)
#     c=b.content.decode('utf-8')
#     m = re.compile('<h2>(.*?)</h2>', re.S)
#     n = m.findall(c)
#     for j in n:
#         ff.append(j)
#     print(len(ff))
#     d=re.compile('<div class="content">(.*?)</span>',re.S)
#     f=d.findall(c)
#     for i in f:
#         i=i.replace('<span>','')
#         i = i.strip()
#         i=i.replace('<br/>','')
#         aa.append(i)
#     print(len(aa))
#     bg = xlwt.Workbook()
#     sheet = bg.add_sheet('pachong')
#     for qq in range(len(ff)):
#         sheet.write(qq*2, 0, ff[qq])
#         sheet.write(qq*2+1,0,aa[qq])
#         bg.save('a.xls')


# 图片的爬取
# import re
# import requests
# class Tupian(object):
#     def 发送请求(self,page):
#         wangzzhi='https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
#         a={
#     'User-Agent':'Mozilla/5.0(Windows NT10.0;Win64;x64;rv:66.0)Gecko/20100101 Firefox/66.0'
#     }
#         res=requests.get(wangzzhi,headers=a)
#         html=res.content.decode('utf-8')
#         return html    #用 return才能将结果传入下面的函数中
#
#     def 过滤(self,abc):
#         lianjie=[]
#         patt=re.compile(r'<div class="thumb">(.*?)</a>',re.S)
#         a=patt.findall(abc)
#         for i in a:
#             new_a=re.compile(r'img src="(.*?)"',re.S)
#             b=new_a.findall(i)
#             lianjie.extend(b)
#         return lianjie
#     def save(self,lianj):    #图片是个链接，请求图片的链接，将其保存下来
#         for a,j in enumerate(lianj):       #接受响应的结果hi能用content
#             res=requests.get('https:'+j)
#             qq=res.content
#             with open('tp\{}.jpg'.format(a),'wb')as qqq:
#                 qqq.write(qq)
# tu=Tupian()
# # 在此加循环，就可以爬取多页的内容
# lv=tu.发送请求(1)     #将上一个函数的结果可以让下一个函数使用
# lj=tu.过滤(lv)          #将结果赋给一个变量，下一个函数调用就可以使用
# tu.save(lj)


# #爬取多页图片
# import re
# import requests
# class douban(object):
#     def wangzhi(self,yeshu):
#         wz='https://movie.douban.com/top250?start={}&filter='.format(yeshu)
#         a={
#             'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv: 66.0)Gecko/20100101Firefox/66.0'
#     }
#         res = requests.get(wz, headers=a)
#         html=res.content.decode('utf-8')
#         return html
#
#     def gg(self,gc):
#         names=[]
#         haibao=[]
#         dym=re.compile('<img width="100"(.*?)<div class="info">',re.S)
#         dyms=dym.findall(gc)
#         # print(dyms)
#         for dd in dyms:
#             ndy=re.compile(r'alt="(.*?)"',re.S)
#             name=ndy.findall(dd)
#             ny=re.compile(r'src="(.*?)" class="">\n',re.S)
#             dhaibao=ny.findall(dd)
#             names.extend(name)
#             haibao.extend(dhaibao)
#         return names,haibao
#     def baoc(self,bc,ac):
#         for a,b in enumerate(ac):
#             qq=requests.get(b)
#             qs=qq.content
#             zz=bc[a]
#             with open('tp\{}.jpg'.format(zz),'wb')as ff:
#                 ff.write(qs)
# db=doub an()
# for an in range(0,100,25):
#     wz=db.wangzhi(an)
#     tl,ij=db.gg(wz)
#     db.baoc(tl,ij)


# # 爬取导演，有多少人评价，电影名称，评分等放入表格中
# import re
# import requests
# import xlrd
# import xlwt
# from xlutils.copy import copy
#
# class douban_name(object):
#     def wangzhi(self,sl):
#         wz='https://movie.douban.com/top250?start={}&filter='.format(sl)
#         leixing={
#             'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv: 66.0)Gecko/20100101Firefox/66.0'
#         }
#         res = requests.get(wz, headers=leixing)
#         html=res.content.decode('utf-8')
#         # print(html)
#         return html
#     def filter(self,ft):
#         director=re.compile('导演:(.*?)&nbsp',re.S)
#         daoyan=director.findall(ft)
#         name=[]
#         movie_name=re.compile(' <div class="pic">(.*?)</a>',re.S)
#         movie_name_1=movie_name.findall(ft)
#         for dy_name in movie_name_1:
#             movie=re.compile(r'<img width="100" alt="(.*?)"',re.S)
#             names=movie.findall(dy_name)
#             name.append(names)
#             # print(names)
#         pingfen=[]
#         pingjia=[]
#         pingfen_2=re.compile('<div class="star">(.*?)</div>',re.S)
#         pingfen_1=pingfen_2.findall(ft)
#         # print(pingfen_1)
#         for pj in pingfen_1:
#             score_1=re.compile('<span class="rating_num" property="v:average">(.*?)</span>',re.S)
#             evaluate = re.compile('<span>(.*?)评价</span>', re.S)
#             pingfen.append(score_1.findall(pj))
#             pingjia.append(evaluate.findall(pj))
#         # print(daoyan)
#         # print(name)
#         # print(pingfen)
#         # print(pingjia)
#         return daoyan,name,pingfen,pingjia
#     def baocun(self,d,n,f,j):
#         try:
#             q=xlrd.open_workbook('bb.xls')
#             sheet=q.sheets()[0]
#             hang=sheet.nrows
#             new_q=copy(q)
#             sheet_1=new_q.get_sheet(0)
#             for k ,kk in enumerate(d):
#                 sheet_1.write(hang+k,0,kk)
#                 sheet_1.write(hang+k,1,n[k])
#                 sheet_1.write(hang+k,2,f[k])
#                 sheet_1.write(hang+k,3,j[k])
#             new_q.save('bb.xls')
#         except:
#             q=xlwt.Workbook()
#             sheet=q.add_sheet('豆瓣电影')
#             sheet.write(0,0,'导演')
#             sheet.write(0,1,'电影名')
#             sheet.write(0,2,'评分')
#             sheet.write(0,3,'评价')
#             for y,xx in enumerate(n):
#                 sheet.write(y+1,0,d[y])
#                 sheet.write(y+1,1,xx)
#                 sheet.write(y+1,2,f[y])
#                 sheet.write(y+1,3,j[y])
#             q.save('bb.xls')
# db=douban_name()
# for aa in range(0,100,25):
#     yshu=db.wangzhi(aa)
#     d,n,f,j=db.filter(yshu)
#     db.baocun(d,n,f,j)


#爬取的任何资源，是一个HTML文件，是静态网页
#动态网页：资源不在HTML文件中，是实时动态刷新的
#加载网页资源   加载网页的方式：1.JavaScript报文都在js中    2.xhr中是ajax报文    带有{}叫json
#json是一种轻量级的数据传输格式   Python 不识别json数据，不识别的都识别为字符串
#json中函数：1.loads：将json格式转换为字典  2.dumps：将字典转换成json格式
#按f12进入浏览器调试工具，——网络——所有——刷新——

# import requests
# import json
#
# wangzhi='https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=13&city=410200&geoobj=114.267502|34.770637|114.448818|34.815759&_src=around&keywords=美食'
# res=requests.get(wangzhi)
# qwe=res.text
# # 1.loads：将json格式转换为字典  2.dumps：将字典转换成json格式
# asd=json.loads(qwe)
# zxc=json.dumps(asd)
# print(asd['data']['poi_list'][2]['address'])  #括号中为过滤条件，要注意是什么数据类型
# print(asd['data']['poi_list'][2]['name'])


#智联招聘  爬取职位，薪资，公司名，公司地址，工作经验，学历
import requests
import json
import xlwt
import xlrd
from xlutils.copy import copy
import smtplib
import email.mime.multipart
import email.mime.text

class zhilian(object):
    def wangzhi(self,qq):
        wz='https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试工程师&kt=3&_v=0.04983607&x-zp-page-request-id=a24e403b64d94c38b7f555c248fa625b-1554119449440-885852'.format(qq)
        a={
            'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv:66.0)Gecko/20100101Firefox/66.0'
        }
        res=requests.get(wz,headers=a)
        html = res.content.decode('utf-8')
        return html
    def guolv(self,guo):
        tj = json.loads(guo)
        aa=len(tj['data']['results'])
        print(aa)
        dz,xz,gjy,gn,zw,xl=[],[],[],[],[],[]
        for ii in range(aa):
            dizhi=tj['data']['results'][ii]['city']['display']
            dz.append(dizhi)
            xinzhi=tj['data']['results'][ii]['salary']
            xz.append(xinzhi)
            workjy=tj['data']['results'][ii]['workingExp']['name']
            gjy.append(workjy)
            gongsi_name=tj['data']['results'][ii]['company']['name']
            gn.append(gongsi_name)
            zhiwei=tj['data']['results'][ii]['jobName']
            zw.append(zhiwei)
            xueli=tj['data']['results'][ii]['eduLevel']['name']
            xl.append(xueli)

        return dz,xz,gjy,gn,zw,xl
    def baocun(self,rr,ee,ss,ff,nn,mm):
        try:
            q=xlrd.open_workbook('b.xls')
            sheet=q.sheets()[0]
            hang=sheet.nrows
            new_q=copy(q)
            sheet_1=new_q.get_sheet(0)
            for k,kk in enumerate(rr):
                sheet_1.write(hang+k,0,kk)
                sheet_1.write(hang+k,1,ee[k])
                sheet_1.write(hang+k,2,ss[k])
                sheet_1.write(hang+k,3,ff[k])
                sheet_1.write(hang+k,4,nn[k])
                sheet_1.write(hang+k,5,mm[k])
            new_q.save('b.xls')
        except:
            q=xlwt.Workbook()
            sheet=q.add_sheet('智联招聘')
            sheet.write(0,0,'公司地址')
            sheet.write(0,1,'薪资')
            sheet.write(0,2,'工作经验')
            sheet.write(0,3,'公司名称')
            sheet.write(0,4,'职位')
            sheet.write(0,5,'学历')
            for y,xx in enumerate(rr):
                sheet.write(y+1,0,xx)
                sheet.write(y+1,1,ee[y])
                sheet.write(y+1,2,ss[y])
                sheet.write(y+1,3,ff[y])
                sheet.write(y+1,4,nn[y])
                sheet.write(y+1,5,mm[xx])
            q.save('b.xls')

zl=zhilian()
for oo in range(0,270,90):
    for kk in range(oo,180,90):
        gl=zl.wangzhi(kk)
        dza, xza, gjya, gna, zwa, xla=zl.guolv(gl)
        zl.baocun(dza,xza,gjya,gna,zwa,xla)

fr='m17630926181@163.com'
res='1959985144@qq.com'
service='smtp.163.com'
password='m17630926181'
message=email.mime.multipart.MIMEMultipart()
message['from']=fr
message['to']=res
message['subject']='主题名'
text='智联招聘'
txt=email.mime.text.MIMEText(text)
message.attach(txt)
aa_1=email.mime.text.MIMEText(open('b.xls','rb').read(),'base64','utf-8')
aa_1["Content-Type"] = 'application/octet-stream'
aa_1["Content-Disposition"] = 'attachment; filename="b.xls"'
message.attach(aa_1)
smtp123 = smtplib.SMTP_SSL(service, 465)
smtp123.login(fr, password)
smtp123.sendmail(fr, res, message.as_string())
smtp123.close()



# def hanshu(zfc,sz_1,sz_2):
#     a=len(zfc)
#     zz=list(zfc)
#     b,c=int(sz_1),int(sz_2)
#     # print(type(a))
#     if c>a-b:
#         for i in zz[b::]:
#             zz.remove(i)
#         print(zz)
#     else:
#         for j in zz[b:c+b]:
#             zz.remove(j)
#         print(zz)
#     # print(aa)
# hanshu('xbhasvfd','3','1 ')


# import requests
# import re
# import xlrd
# import xlwt
# from xlutils.copy import copy
#
#
# class boss(object):
#     def we(self,website):
#         wangzhi='https://www.zhipin.com/c101210100/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&page={}&ka=page-{}'.format(website,website)
#         aa={
#             'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:66.0)Gecko/20100101Firefox/66.0'
#         }
#         res=requests.get(wangzhi,headers=aa)
#         htmo=res.content.decode('utf-8')
#         return htmo
#
#     def guolv(self,gl):
#         tiaojian=re.compile(r'<div class="job-primary">(.*?)</h3>',re.S)
#         gg =tiaojian.findall(gl)
#         zw,xz,dz,xl,gsm=[],[],[],[],[]
#         for i in gg:
#             zhiwei=re.compile(r'<div class="job-title">(.*?)</div>',re.S)
#             zhi=zhiwei.findall(i)
#             zw.append(zhi)
#             xinzhi=re.compile(r'<span class="red">(.*?)</span>',re.S)
#             xin=xinzhi.findall(i)
#             xz.append(xin)
#             dizhi=re.compile(r'</h3><p>(.*?)<em class="vline"></em>',re.S)
#             di=dizhi.findall(i)
#             dz.append(di)
#             xueli=re.compile(r'<em class="vline"></em>(.*?)<em class="vline">',re.S)
#             xue=xueli.findall(i)
#             xl.append(xue)
#             gongshi= re.compile(r'custompage" target="_blank">(.*?)</a', re.S)
#             gong=gongshi.findall(i)
#             gsm.append(gong)
#         print(xl)
#         return zw,xz,dz,xl,gsm
#
#     def baocun(self,bc,aa,bb,cc,dd,):
#         try:
#             ff = xlrd.open_workbook('b.xls')
#             sheetl=ff.sheets()[0]
#             num =sheetl.nrows
#             new_f= copy(ff)
#             sheet=new_f.get_sheet(0)
#             for j,k in enumerate(bc):
#                 sheet.write(j+num,0,k)
#                 sheet.write(j+num,1,aa[j])
#                 sheet.write(j+num,2,bb[j])
#                 sheet.write(j+num,3,cc[j])
#                 sheet.write(j+num,4,dd[j])
#
#             new_f.save('b.xls')
#         except:
#             f = xlwt.Workbook()
#             sheet = f.add_sheet('boss直聘')
#             sheet.write(0, 0,'职位')
#             sheet.write(0, 1,'薪资')
#             sheet.write(0, 2,'公司地址')
#             sheet.write(0, 3,'工作经验')
#             sheet.write(0, 4,'学历')
#
#             for j,k in enumerate(bc):
#                 sheet.write(j+1,0,k)
#                 sheet.write(j+1,1,aa[j])
#                 sheet.write(j+1,2,bb[j])
#                 sheet.write(j+1,3,cc[j])
#                 sheet.write(j+1,4,dd[j])
#
#             f.save('b.xls')





# bs=boss()
# for ii in range(3):
#     ys=bs.we(ii)
#     a,b,c,d,e=bs.guolv(ys)
#     bs.baocun(a,b,c,d,e)





