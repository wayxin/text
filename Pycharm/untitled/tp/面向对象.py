# 面向对象：将函数进行分类和封装，使开发更高效      只是一种编程思想

#面向对象和面向过程的区别
#类名规则和函数名规则一样 （为了与函数名区分，默认的类名首字母大写）
# 在python中不叫面向对象，叫类
# 1.，类（class）  创建一个类 class
# 2.对象，类的实例    通过赋值，产生类的实例，也叫一个对象    方便在类的外部调用函数
#self   不属于函数的参数，self类的实例，方便在类的内部调用函数   不同的类之间的self不能相互调用
# 优点：方便管理代码
# # 格式：
# class 小艾():#类名    #类中都是函数，都归类管
#     def 打电话(self):#函数名
#         pass
#         self.播放音乐()
#     def 播放音乐(self):#函数名
#         pass
# class qwe():
#     def aini(self):
#         print('cdbh')
#         self.asd()
#         self.zxc()
#     def asd(self):
#         print('odueb')
#     def zxc(self):
#         print('98137')
#     # 调用类里面的函数
# x=qwe()    #x(赋给的对象)叫做类的实例、类的对象
# x.aini()

#3.  继承：就是新的类继承旧的类中所有的函数   类名（继承的旧类名）
# 例
# class qwe():
#     def aini(self,a,b=0):#self后可以跟默认参数和其他参数
#         print('cdbh')
#         print(a)
#     def asd(self):
#         print('odueb')
#     def zxc(self):
#         print('98137')
# class abc():
#     pass
# class hg():
#     def nmt(self):
#         print('nainiyou')
# class poi(qwe,hg):     #继承多个类时，中间应逗号隔开,两个类中能够有函数重复，只取第一个类中的
#     print('qq')
# x=poi()
# x.aini(1927)

#4.多态（函数重写）
# class qwe():
#     def aini(self,a,b=0):
#         print('cdbh')
#         print(a)
#     def asd(self):
#         print('odueb')
#     def zxc(self):
#         print('98137')
# class abc(qwe):
#     def aini(self,a,b=0):
#         print('cdbh')
#         print(a)
#         print('cbwyduvc')    #将上面的类继承下来，更改其中某些函数的功能，下面的类就将上面的类给覆盖掉了
# x=abc()
# x.aini(1927)

#5. 私有方法     将类中的函数变成私有函数，不允许被继承
                         #在函数名前加两个下划线  只能在类的内部调用
# class qwe():
#     def __aini(self):
#         print('cdbh')
#     def asd(self):
#         print('odueb')
#         self.__aini()
# class abc(qwe):
#     def dsd(self):
#         print('cbwyduvc')
# x=qwe()
# x.asd()

#  6.专有函数  左右都带有下划线的函数，叫类的专有函数
# 任何一个类中都有属性（类中的方法具有的共同特点）和方法（函数）
# __init__    初始化属性   相当于传参（在调用类括号中传参）
# class qwe():
#     name='小刚'   #属性
#     def __init__(self,a):   #初始化属性   可以传入属性
#         self.name=a
#     def aini(self):
#         print('cdbh{}'.format(self.name))
#     def asd(self):
#         print('odueb{}'.format(self.name))
# x=qwe('小米')      #数据填在类的调用中
# x.asd()








