#! /usr/bin/python
# -*- coding:utf-8 -*-
import smtplib#封装了smtp协议
import email.mime.multipart#处理邮件中的组成部分
import email.mime.text#处理文件中的正文
#设置发件人
fr='15903893872@163.com'
#设置收件人
res='969598484@qq.com'
#设置服务器
server='smtp.163.com'
#设置密码
password='lgs418710'
#设置一个空邮件
mes=email.mime.multipart.MIMEMultipart()
#添加发件人
mes['from']=fr
#添加收件人
mes['to']=res
#添加主题
mes['Subject']='日报'
#设置正文
text="哈哈哈哈哈 \n  你好啊"
#处理及添加正文
txt=email.mime.text.MIMEText(text)
mes.attach(txt)
# 添加附件
att2 = email.mime.text.MIMEText(open('a.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="a.txt"'
## 头部字段
mes.attach(att2)
#定义服务器
smtp123=smtplib.SMTP_SSL(server,465)
#登陆服务器
smtp123.login(fr,password)
#发送邮件
smtp123.sendmail(fr,res,mes.as_string())
#断开连接
smtp123.close()