





# os是一个自带的库，是与操作系统交互的   通过os模块来控制操作系统

import os
#删除文件
# os.remove('文件名')
#ping网址  执行Windows命令  括号中写Windows命令
# a=os.popen('ping 192.168.1.12')
# print(a.read())
#获取当前所在位置
# a=os.getcwd()
# print(a)
# #切换目录
# b=os.chdir(r'F:')
# a=os.getcwd()
# print(a)
#获取当前文件夹下文件  括号中写要获取的文件夹路径
# a=os.listdir('.')
# print(a)

# 将当前文件夹下的.py文件打印出来
# a=os.listdir('.')
# b='.py'
# for i in a:
#     if b in i:
#         print(i)

#将文件与路径与文件分割开
# q=os.path.split(r'‪C:\Users\Public\Desktop\微信.lnk')
# print(q)
#将文件后缀名与前面路径分割开
# q=os.path.splitext(r'‪C:\Users\Public\Desktop\微信.lnk')
# print(q)
#判断文件是否为目录
# a=os.path.isabs('wenjain')    不是在本目录下要加路径
# print(a)
#判断文件是否是个普通文件
# b=os.path.isfile('bb.xls')
# print(b)

#创建文件夹
# os.mkdir('aaa')
# #创建递归文件夹
# os.makedirs('bbb/ccc/ddd')
# #删除空文件夹
# os.rmdir('aaa')
# #删除递归空文件夹
# os.removedirs('bbb/ccc/ddd')



#封装ssh协议，可以实现远程控制
# import paramiko
# #创建一个远程客户端
# ssh123=paramiko.SSHClient()
# #跳过验证，不到know_hosts文件中取查找
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #链接主机
# ssh123.connect(hostname='192.168.1.28',
#                port=22,
#                username='wy',
#                password='123456')
# stuin,stuout,stuerr=ssh123.exec_command('ls -al')
# #stuin:执行命令    只能执行有结果的命令
# #stuout:执行结果
# #stuerr:执行报错
# print(stuout.read().decode())
# #关闭远程控制
# ssh123.close()

# import paramiko
#传输文件
#建立一个传输通道
# ssh123=paramiko.Transport(('192.168.1.28',22))
#链接主机,
# ssh123.connect(username='wy',password='123456')
#创建一个sftp客户端
# sftp=paramiko.SFTPClient.from_transport(ssh123)
#从liunx下载文件到windows
# sftp.get('路径+文件名','存放本地位置，可以改名')   #第一个参数为要下载的文件，第二个为存储的本地位置
# 将Windows上传到liunx中
# sftp.put('DAY1.py','day1.py')    #第一个参数为本机文件，第二个参数为要上传到liunx上的路径
# ssh123.close()

# import paramiko
# ssh123=paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname='192.168.1.28',
#                port=22,
#                username='wy',
#                password='123456')
# while True:
#     mingling=input('输入liunx命令：')
#     if mingling=='exit':
#         break
#     try:
#         stuin,stuout,stuerr=ssh123.exec_command(mingling)
#         print(stuout.read().decode())
#         # ssh123.close()
#     except:
#         continue




#包与模块的区别
#模块是一个.py文件，封装的是代码
#包是一个目录，封装的是模块，必须含有__init__.py文件
#面向对象与面向过程的区别
#面向对象：将函数进行分类和封装，使开发更高效，容易扩展（加功能，添加函数），易于维护（有利于修改错误），性能比较低
#面向过程：一步一步实现解决问题的步骤，性能高，不易扩展，不易维护

# import smtplib   #封装SMTP协议
# import email.mime.multipart   #处理邮件中的组成部分  收件人  主题等
# import email.mime.text      #处理邮件的正文
# #发件人
# fr='m17630926181@163.com'
# #收件人
# res='18317822978@163.com'
# #服务器
# service='smtp.163.com'    #发送人为163邮箱
# #授权码  授予登录客户端的权限的密码
# password='m17630926181'
# #创建一个空邮件
# message=email.mime.multipart.MIMEMultipart()
# #给邮件添加一个发件人
# message['from']=fr    #可以直接填邮箱
# #添加一个收件人
# message['to']=res   #也可以直接添加收件人邮箱
# #添加一个主题
# message['subject']='python learn'
# #添加邮件正文
# text='春天该很好，你若尚在场，一生未见，一世怀念'
# #处理正文
# txt=email.mime.text.MIMEText(text)
# message.attach(txt)
# # 添加附件，附加的文件（图片，软件，表格等也可以发送）
# att2 = email.mime.text.MIMEText(open('a.xls', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'    #头部字段
# att2["Content-Disposition"] = 'attachment; filename="a.xls"'
# ## 头部字段
# message.attach(att2)
# #定义服务器
# smtp123=smtplib.SMTP_SSL(service,465)  #括号中为定位的服务器和端口号
# #登录服务器
# smtp123.login(fr,password)    #用户名  授权码
# #发送邮件
# smtp123.sendmail(fr,res,message.as_string())  #发送者，收件人，处理后的正文
# #断开连接
# smtp123.close()


#客户端
# import socket
# #1.创建一个套接字
# sock=socket.socket()
# #客户端不需要绑定IP和端口号，只需要建立连接，要再电脑可以运行有网的情况下
# #2.服务器的IP和端口号
# sock.connect(('192.168.1.5',80))
# #3.发送请求
# msg='hi!'
# sock.send(msg.encode('utf-8'))
# #4.接受请求
# reg=sock.recv(1024)
# print(reg.decode('utf-8'))
# #5.断开连接
# sock.close()


# UDP客户端
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#UDP不需要建立连接,要写服务器的IP地址和端口号
host=('192.168.1.5',809)
msg='hi!'
s.sendto(msg.encode('utf-8'),host)
reg=s.recv(1024)
print(reg.decode('utf-8'))
s.close()








# import socket
# while True:
#     sock=socket.socket()
#     sock.connect(('192.168.1.18',51000))
#     msg=input('>>>')
#     sock.send(msg.encode('utf-8'))
#     reg=sock.recv(1024)
#     print(reg.decode('utf-8'))
