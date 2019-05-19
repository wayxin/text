





# #在虚拟机的MySQL中给数据库赋予权限，关闭防火墙
# import pymysql
# # connect:链接数据库
# sjk=pymysql.connect(host='192.168.1.28',
#                 port=3306,
#                 user='root',
#                 passwd='123456')
# # cursor:创建游标   类似于vim中的光标
# yb=sjk.cursor()
# #execute:执行SQL语句
# yb.execute('show databases;') #打印的为数据库的个数
# # yb.execute('create database day_one;')  #创建一个库
# yb.execute('use day_one;')          #进入一个数据库
# yb.execute('create table aa(姓名 char(255),年龄 int,性别 char(255),成绩 int);')    #在数据库中添加表
# yb.execute('insert into aa values ("张三",19,"男",78),("王五",20,"女",89);')     #在表中插入数据
# # #循环加入数据
# # for i in range(100) :
# #     yb.execute('insert into day_one values ("{}",{},"{}",{});'.format("片名","导演","评价","评分"))
# sjk.commit()     #添加数据要提交   更新，删除，添加时最好提交一下
# yb.execute('select * from aa;')          #查看表中数据
# #fetchall：获取到上一个SQL语句的结果
# a=yb.fetchall()      #打印的才是想要的内容
# #fetca=yb.fetchall() hmany；获取上一个SQL语句的结果，默认只获取结果的第一个数据，可加参数，可以获取参数个数的数据
# # a=yb.fetchmany(3)
# #fetchone:每次只获取一条结果，有迭代的功能，第二个获取的是第二条结果
# # a=yb.fetchone()
# # b=yb.fetchone()
# print(a)
# #断开连接
# sjk.close()





# import pymysql
# import re
# import requests
# sjk=pymysql.connect(host='192.168.1.28',
#                 port=3306,
#                 user='root',
#                 passwd='123456')
# while True:
#     youbiao=sjk.cursor()
#     mingling=input('数据库命令：')
#     if mingling=='exit':
#         break
#     try:
#         youbiao.execute(mingling)
#         a = youbiao.fetchall()
#         print(a)
#     except:
#         continue




#socket   又称为套接字，是提供了通信双方最底层的功能（发送和接受
# 只负责在通信是的接受个发送数据
#用socket实现两台主机进行通信
#服务器
# import socket
# #1.创建一个套接字，创建一个有接受和发送能力的对象,默认使用的为TCP
# # s=socket.socket(socket.SOCK_STREAM)   #括号中使用的为TCP，括号中不填，也是默认使用TCP
# # s=socket.socket(socket.SOCK_DGRAM)     #使用的UDP
# #使用的是IPv4地址和TCP协议，如果括号中不填写，默认使用的也是IPv4和TCP协议
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #2.绑定IP地址和端口#绑定的是一个元组，要再加个括号
# s.bind(('192.168.1.5',80))
# #3.监听服务有没有开启
# s.listen(33)  #括号中为最大等待个数，接受最大连接数跟服务器的性能有关，与括号中数字无关
#
# while True:
#     #4,接受请求,建立连接
#     client,addr=s.accept()   #第一个值为建立连接的信息，第二个值为客户端的IP地址和端口号
#     #5.接受客户端发送的请求,1024为每次接受最大的字节
#     msg=client.recv(1024)
#     print(msg.decode('utf-8'))   #decode  解码
#     #6.发送响应
#     reg='hello'
#     client.send(reg.encode('utf-8'))      #encode 编码


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.1.5',80))
# s.listen(3)
#
# while True:
#     client,addr=s.accept()
#     msg=client.recv(1024)
#     print(msg.decode('utf-8'))
#     reg=input('>>>')
#     client.send(reg.encode('utf-8'))



#通过UDP建立连接
#服务器端
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('192.168.1.5',809))
# #不需要监听
# # s.listen(3)
# while True:
#     #接受 第一个为客户端的请求数据，第二个为客户端的IP和端口号
#     client,addr=s.recvfrom(1024)
#     print(client)
#     print(addr)
#     print(client.decode('utf-8'))
#     msg='hello'
#     #发送，发送给addr
#     s.sendto(msg.encode('utf-8'),addr)
#
# import pymysql
# import re
# import requests
# sjk=pymysql.connect(host='192.168.1.28',
#                     port=3306,
#                     user='yx',
#                     passwd='123456')
# yb=sjk.cursor()
# yb.execute('use day_one;')
# yb.execute('creat table test_tab(zhi_1 char(255),zhi_2 char(255),zhi_3 char(255),zhi_4 char(255);')
# aa=yb.fetchall()
# # yb.execute('insert into test_tab')
# # # bb=yb.fetchall()
# # # yb.execute()
# sjk.commit()
#
# print(aa)

