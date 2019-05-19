#! /usr/bin/python
# -*- coding:utf-8 -*-
# import pymysql
# # 连接数据库
# conn=pymysql.connect(host='192.168.2.115',port=3306,user='root',passwd='123456')
# mysqla=conn.cursor()
# while True:
#     a=input('>>')
#     if a=='exit':
#         print('byby')
#         break
#     try:
#         mysqla.execute('{}'.format(a))
#         conn.commit()
#         b=mysqla.fetchall()
#         print(b)
#     except:
#         while True:
#             print('sql语句有错请重新输入')
#             break