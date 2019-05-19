#！/use/bin/python
#* -*- coding:utf-8 -*-
# #向表格中写入数据   用xlwt模块
# import xlwt
# #1.打开一个表格文件
# f=xlwt.Workbook()    #由标签页管理   括号中跟编码方式可跟可不跟
# #2.添加一个标签页
# sheet= f.add_sheet('日报')    #括号中为标签页名称
# #3.向标签页张红写入数据
# #  括号中第一个为行，默认从零开始
# #  第二个为列，默认从0开始
# #  第三个为插入的数据内容
# sheet.write(0,0,'日常')
# #4.保存文件   括号中为文件名
# f.save('a.xls')
#读取表格中数据
# import xlrd    #xlrd模块
#打开读取的表格文件
# f=xlrd.open_workbook('a.xls')
#获取文件中有多少个标签页
# b=f.nsheets
# print(b)
# #获取表格中所有标签页的名称
# a=f.sheet_names()
# print(a)
#进入要读取的标签页
# sheet=f.sheet_by_name('标签页名称')  #通过标签页名称进入要读取的标签页
# sheet=f.sheets()[0]   #通过下标位置索引进入操作的标签页
# #文件红有多少行
# c=sheet.nrows
# #循环文件中共多少行内容
# for i in range(1,3):
#     d=sheet.row_values(i)   #读取标签页中的第几行
#     print(d)

#获取标签页中有多少行
# c=sheet.ncols
# #读取标签页中的第几列
# for i in range(1,3):
#     b=sheet.col_values(i)
#     print(b)
#获取某个格子里的数据
# b=sheet.cell(3,0).value
# print(b)


#
#添加30行30列内容
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('pyton_test')
# for i in range(15):
#     for j in range(6):
#         sheet.write(i,j,'123')
# f.save('a.xls')

# 将九九乘法表写入表格中
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('pyton_test')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i,j,'{}*{}={}'.format(i,j,i*j))
# f.save('a.xls')


# f=open(r'DAY1','r',encoding='utf-8')
# a=f.read()
# b=a.split('\n')
# e=[]
# import xlwt
# h=xlwt.Workbook()
# sheet=h.add_sheet('学员表')
# for i in range(4):
#     x=b[i]
#     e=x.split(',')
#     for j in range(3):
#         sheet.write(i,j,'{}'.format(e[j]))
# h.save('a.xls')

# import xlwt
# f=open(r'DAY1','r',encoding='utf-8')
# f=f.read()
# d=f.split('\n')
# y=len(d)
# q=xlwt.Workbook()
# sheet=q.add_sheet('学员表')
# for b in range(y):
#     m=d[b]
#     e=m.split(',')
#     p=len(e)
#     for n in range(p):
#         sheet.write(b,n,e[n])
# q.save('a.xls')

# 将文件写入到表格中
# import xlwt
# with open('DAY1','r',encoding='utf-8') as f:
#     a=f.readlines()
# q=xlwt.Workbook()
# sheet=q.add_sheet('xue')
# for i in range(len(a)):
#     m=a[i]
#     s = m.split(',')
#     for j in range(len(s)):
#         sheet.write(i,j,s[j])
# q.save('a.xls')

# 将表格中数据写入到文件中
# import xlrd
# f=xlrd.open_workbook('a.xls')
# sheet=f.sheets()[0]
# h=sheet.nrows
# l=sheet.ncols
# with open('a.txt','w',encoding='utf-8')as ff:
#     for i in range(h):
#         for j in range(l):
#             b=sheet.cell(i,j).value
#             ff.write(b+' ')
#         ff.write('\n')

# from xlutils.copy import copy
# import xlrd
# #打开一个文件
# f=xlrd.open_workbook('a.xls')
# #复制文件
# new_f=copy(f)
# #获取要操作的标签页
# sheet = new_f.get_sheet(0)#   括号中是根据下标位置获取标签页
# #在复制的文件中添加内容
# sheet.write(5,0,'cgv')
# #保存文件
# new_f.save('a.xls')


#时间模块
import time
#时间戳   表示的是从公元一九七零年到现在所经过的秒数
# a=time.time()
# print(a)
#以元组的格式显示本地时间
# a=time.localtime(29831030)    #默认为本地时间，传入参数（只接受时间戳）   显示的为传入参数的时间
# print(a)
#星期几（Python中从零开始）今天是今年的第几天（西方日历1月1日开始算）是否是夏令时 0为夏令时，1为冬令时

#以本地化时间打印
#如果传入参数（元组时间），显示的是传入的参数的时间
# b=time.strftime('%Y-%m-%d %H:%M:%S %w')
# print(b)

#将现代时间转换为元组时间
#括号中为更改的时间，后跟的占位符要与前面的年月日格式一样
# a=time.strptime('2010-12-1 ','%Y-%m-%d')
# print(a)

#将元组的时间转换成时间戳
# a=(1999,2,23,24,13,14,11,15,28)   #必须为九个数据
# b=time.mktime(a)
# print(b)


#休眠时间
# time.sleep(2)

# for i in range(10):
#     print(i)
#     time.sleep(i)

#判断一个日期是否为闰年，查看是星期几，是这一年的第几天
# import time
# a=input('请输入一个日期：')
# b=time.strptime(a,'%Y-%m-%d')
# print(b)
# c=int(b[0])
# print('今天是星期{}'.format(b[-3]+1))
# print('今天是今年的第{}天'.format(b[-2]))
# # print(type(c))
# if c%4==0 or c%400==0:
#     print('是闰年')
# else:
#     print('不是闰年')

# 输入一个日期，打印前一天的日期
# import time
# a=input('请输入一个日期：')
# b=time.strptime(a,'%Y-%m-%d')
# c=[]
# for i in b:
#     c.append(i)
# c=tuple(c)
# m=time.mktime(c)
# n=m-86400
# v=time.localtime(n)
# print(v)

#正则表达式
# import re
# a='qwnfcv4732e52rfed31'
#1.complie  编译  编译成正则语言
# p=re.compile('f(.*)f')   #想要查找指定的内容，给正则条件要加上括号
# print(p)
#2.findall   从某个地方查找所有符合正则的字符串   （两种用法）
#本身有编译的功能
#如果有两个参数：1.第一个为正则表达式的条件，2.第二个是查找范围
#如果只有一个参数的时候，为查找范围，但要在findall前加上条件的参数
# c=re.findall(p,a)  #p为正则查找的条件，将条件也可以直接写入findall里面   a为要查找的文件
# c=p.findall(a)    #a为查找范围，但要在findall前加上的参数是正则的条件
# print(c)
#3.贪婪模式与非贪婪模式
#贪婪模式：尽可能去匹配更多的内容
# n='qweq12q323q'
# m=re.compile('q(.*)q')  #从第一个开始一直取到最后一个中间的所有内容
# x=m.findall(n)
# print(n)                  #正则表达式中的 . 是匹配除换行符和回车以外的所有字符
                           #re.S   是给 . 加功能的，可以让 . 匹配上任意字符
                           #re.I    给条件加功能，不区分大小写
#非贪婪模式：尽可能去匹配更少的内容
# n='qweQ12q323Q'
# m=re.compile('Q(.*?)q',re.I)   #从第一个开始取到第二个之间的内容，然后从第三个去到第四个之间的内容
# x=m.findall(n)
# print(x)















