# -*- coding: utf-8 -*- 

# @Time : 2019/4/29 下午2:22 

# @Author : 废柴 

# @Project: D_sound

# @FileName : func_1.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================
# from src.base import 
import yaml


# 打开定位元素文件
with open('/Users/oldman/D_sound/src/element/item.yaml', 'r', encoding='utf-8') as fb:
    item_data = yaml.load(fb)
    print(item_data)
    print(type(item_data))
# def check_text(argument,a, b):
#     text =argument.find_element_by_id(item_data['three'][a]).find_element_by_class_name \
#         (item_data['ut']['TextView_classs']).text
#     # 格式化字符串的三种写法
#     argument.assertEqual(text, u'%s'%(b))
#     argument.assertEqual(text, f'{b}')
#     argument.assertEqual(text, '{}'.format(b))





