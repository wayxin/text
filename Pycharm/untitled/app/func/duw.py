#! /usr/bin/python
#- -*- coding:utf-8 -*-

import yaml
with open(r'H:\PycharmProjects\untitled\app\element\itml.yaml','r',encoding='utf-8')as f:
    item_data=yaml.load(f,Loader=yaml.FullLoader) # 使用yaml模块的load方法将yaml文件中的数据转换为Python字典的形式
    # print(item_data['three']['wx_id'])

def aa(a):
    wenben_1 = a.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
    print(wenben_1)
    return wenben_1
def bb(a):
    wenben_2 = a.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
    print(wenben_2)
    return wenben_2
def cc(a):
    wenben_3 = a.find_element_by_id(item_data['three']['qq_id']).find_element_by_class_name(item_data['TextView_class']).text
    print(wenben_3)
    return wenben_3
def dd(a):
    wenben_4 = a.find_element_by_id(item_data['three']['pd_id']).find_element_by_class_name(item_data['TextView_class']).text
    print(wenben_4)
    return wenben_4