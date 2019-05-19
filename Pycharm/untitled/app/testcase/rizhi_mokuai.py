#! /usr/bin/python
#- -*- coding:utf-8 -*-
import os
import logging
import datetime

logs=os.path.join(r'H:\PycharmProjects\untitled\app\logs',str(datetime.datetime.now().date())+'.out')
print(logs)
ffo=logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S')
print(ffo)
con_handler=logging.StreamHandler()
con_handler.setFormatter(ffo)

fil_handler=logging.FileHandler(logs,encoding='utf-8')
#加载日志格式
fil_handler.setFormatter(ffo)

def get_log(name):
    #获取脚本的名字传入日志中
    logger=logging.getLogger(name)
    #加入一个手柄，可以在文件中写日志
    logger.addHandler(con_handler)
    logger.addHandler(fil_handler)
    #设置日志的等级 INFO是轻微性日志及包含一二三级
    logger.setLevel(logging.INFO)
    return logger
go=get_log('rizhi_mokuai.py')
go.info('nrezg')