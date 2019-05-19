# -*- coding: utf-8 -*- 

# @Time : 2019/4/28 下午4:24 

# @Author : 废柴 

# @Project: D_sound

# @FileName : base.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

"""
项目配置脚本
"""
import os
# -*- coding: utf-8 -*-

# @Time : 2019/3/15 下午1:44

# @Author : 废柴

# @Project: kyb

# @FileName : setings.py

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

import os

# 获取当前文件的绝对路径

a = os.path.dirname(os.path.abspath(__file__))
print(a)


# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 日志目录
LOG_DIR = BASE_DIR + '/logs/'

# 报告目录
REPORT_DIR = BASE_DIR + '/report/'

# 源文件目录
SRC_DIR = BASE_DIR + '/src/'

# 测试用例目录
TEST_CASE = BASE_DIR + '/testcase/'

# 页面方法目录
FUNC = BASE_DIR + '/func/'

# 公共目录
UNTIL = BASE_DIR + '/until/'

# 测试文件类型
DATA_FILE_TYPE = {
    'yaml': 0,
    'json': 1,
    'xls': 2,
}

# 生成测试报告类型
REPORT_FILE_TYPE = {
    'html': 0,
    'xls': 1,
}
