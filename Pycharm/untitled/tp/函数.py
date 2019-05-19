#！/usr/bin/python
#* -*- coding:utf-8 -*-

#   ###########   函数   #############
# 函数是具有某种功能的，可以重复使用的代码块
# 一.格式： def 函数名（）
#              代码块
# 所有的函数不调用就不会执行
# 调用函数：  函数名（）
# 二.函数名的命名规则：    （与变量名的规则一样）
# 1.只能是字母数字下划线组成
# 2.不能以数字开头
# 3.不能命名成python中的函数
# 三.变量的作用域
#   局部变量：只能作用于局部内容
#   全局变量：任何内容都能使用
# global:将局部变量变成全局变量
# id:查找变量在内存中的位置
#
# 四.参数传递
# 优先级：1>2>3
# 1.必须参数：必须传入的参数（不传入就会报错）    def  函数名（参数名）
# a=lambda x:x+2
#
# def x(a):
#     b=0
#     for i in range(a+1):
#         b=i+b
#     # print(b)
#     return  b
# x(50)
# 2.默认参数（非必须传入的参数）        def    函数名（参数名=值）
# 传入数据的个数必须与参数的个数相等
# def x(a=100):
#     b=0
#     for i in range(a+1):
#         b=i+b
#     print(b)
# x(18)
# 3.可变长参数（非必须参数）       def    函数名（*参数名）或（**参数名）   默认的参数名称为args
# def x(*args):                # 默认的参数名称为args         打印格式为元组
# def n(**kwargs):              #默认的参数名称为kwargs      打印格式是键值对格式
# def x(a,*args,b=19):     #优先级：必须参数 > 默认参数 > 可变长参数
#     print(a)
#     print(b)
#     print(args)
# x(18,12,873,8,8,9,1,3,4)
# 五.结果返回
#     return   1.函数的结束    2.赋值给调用者
#     函数的功能不变，计算1到任何数的和 ，最后的值加2
# def x(b):
#     a=0
#     for i in range(1,b+1):
#         a=a+i
#     print(a)
#     return a         #可以附多个值，打印的格式为元组
#                      #当附多个值时，也可以有多个变量
# c=x(100)      #调用代码：只有一个功能就是调用函数，本身是没有任何数据的
# print(c+2)
# 六、匿名函数
# lambda#  只是一个表达式 作用：来定义一个具有某种功能，可重复使用的代码块
# lambda与def的区别：
# lambda简单，表达式，描述不了复杂，逻辑结构强的代码
# 格式：函数名 = lambda 参数：表达式
# eg:
#lambda乘法计算
# x=lambda a,b=4:a*b
# print(x(7))
#
# y=lambda a,b=8,*args:a+b and args
# print(y(9,7,31,8,19,4,))


# def x(a,b=19,*args):     #优先级：必须参数 > 默认参数 > 可变长参数
#     print(a)
#     print(b)
#     print(args)
# x(18,12,873,8,8,9,1,3,4)
#
# # add=lambda i,j:i+j
# # print(add(12,9))
#                   #lambda可以简单化def的句子
# def add(i,j):
#     return i+j
# print(add(12,9))
i=0
a=0
while i<101:
    i=i+1
    a=a+i
print(a)



