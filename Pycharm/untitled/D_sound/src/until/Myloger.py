# -*- coding: utf-8 -*- 

# @Time : 2019/4/28 下午4:31 

# @Author : 废柴 

# @Project: D_sound

# @FileName : Myloger.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================
from src.base import LOG_DIR, os
import logging
import datetime

# 创建一个日志文件
logs = os.path.join(LOG_DIR, str(datetime.datetime.now().date()) + ".out")
# 个性化日志文件的输出格式
formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',
                              datefmt='%d-%m-%Y:%H:%M:%S')
# 将日志设置为字节流形式，用于控制台输出日志信息
con_handler = logging.StreamHandler()
# 加载个性化日志输出的格式
con_handler.setFormatter(formatter)
# 将日志输出到文本
fil_handler = logging.FileHandler(logs, encoding='utf-8')
# 加载个性化日志输出的格式
fil_handler.setFormatter(formatter)

# 定义日志等级，设置日志句柄，供其他对象调用
def get_logger(name):
    logger = logging.getLogger(name)
    logger.addHandler(con_handler)
    logger.addHandler(fil_handler)
    logger.setLevel(logging.INFO)
    return logger