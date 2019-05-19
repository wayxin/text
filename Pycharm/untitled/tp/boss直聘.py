#!/use/bin/python
# -*- coding:utf-8 -*-

#boss直聘：

import requests
import re
import xlwt
import xlrd
from xlutils.copy import copy
class Boss(object):
    def qingqiu(self,yeshu):
        wz='https://www.zhipin.com/c101210100-p100302/?page={}&ka=page-{}'.format(yeshu,yeshu)
        zhidian = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
                        }
        fs=requests.get(wz,headers=zhidian)
        wy=fs.content.decode('utf-8')
        # print(wy)
        return wy
    def guolv(self,ab):
        tj=re.compile(r'<div class="job-primary">(.*?)></h3>',re.S)
        gl=tj.findall(ab)
            # print(gl)
        acc,aaa,bbb,ccc,xueli,eee=[],[],[],[],[],[]
        for i in gl:
            tjz=re.compile(r'<div class="job-title">(.*?)</div>\n',re.S)
            zy=tjz.findall(i)
            tjx=re.compile(r'<span class="red">(.*?)</span>\n',re.S)
            xz=tjx.findall(i)
            tjd=re.compile(r'<p>(.*?)<em class="vline"></em>',re.S)
            dz=tjd.findall(i)
            tjj=re.compile(r'<em class="vline"></em>(.*?)<em class="vline">',re.S)
            jy=tjj.findall(i)
            tjxl=re.compile(r'(大专|本科|学历不限|硕士|中专/中技)',re.S)
            xl=tjxl.findall(i)
            tjdz=re.compile(r'custompage" target="_blank">(.*?)</a',re.S)
            gs=tjdz.findall(i)
            acc.append(zy[0])
            aaa.append(xz[0])
            bbb.append(dz[0])
            ccc.append(jy[0])
            xueli.extend(xl)
            eee.append(gs[0])

        return acc,aaa,bbb,ccc,xueli,eee
    def baocun(self,bc,aa,bb,cc,dd,ee):
        try:
            ff = xlrd.open_workbook('b.xls')
            sheetl=ff.sheets()[0]
            num =sheetl.nrows
            new_f= copy(ff)
            sheet=new_f.get_sheet(0)
            for j,k in enumerate(bc):
                sheet.write(j+num,0,k)
                sheet.write(j+num,1,aa[j])
                sheet.write(j+num,2,bb[j])
                sheet.write(j+num,3,cc[j])
                sheet.write(j+num,4,dd[j])
                sheet.write(j+num,5,ee[j])
            new_f.save('b.xls')
        except:
            f = xlwt.Workbook()
            sheet = f.add_sheet('boss直聘')
            sheet.write(0, 0,'职位')
            sheet.write(0, 1,'薪资')
            sheet.write(0, 2,'公司地址')
            sheet.write(0, 3,'工作经验')
            sheet.write(0, 4,'学历')
            sheet.write(0, 5,'公司名称')
            for j,k in enumerate(bc):
                sheet.write(j+1,0,k)
                sheet.write(j+1,1,aa[j])
                sheet.write(j+1,2,bb[j])
                sheet.write(j+1,3,cc[j])
                sheet.write(j+1,4,dd[j])
                sheet.write(j+1,5,ee[j])
            f.save('b.xls')
for p in range(1,6):
    h=Boss()
    f=h.qingqiu(p)
    v,a,b,c,d,e=h.guolv(f)
    h.baocun(v,a,b,c,d,e)