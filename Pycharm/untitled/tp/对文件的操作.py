

#对文件的操作     open() 函数
#格式：  变量名=# open(文件名，权限，编码方式)
#文件名：1.

#转义字符：|t    |n
#报错的原因：路径中有转义字符
#注：在写文件路径时，要注意转义
#1、在反斜杠前加一个反斜杠  2、在路径前加r

# f=open(r'DAY1.py','r',encoding='utf-8')
# print(f.read())
#权限：对文件的操作权限
#包括：写(w)覆盖式的写入、读(r)、追加(a)
#     w+     r+     a+    （wb    rb     ab）以二进制的方式读取和写入
     #当使用的文件为w或a时，操作的文件如果存在就直接写入，如果不存在就先创建文件，再写入
#      最好对文件的操作完成之后关闭文件
#      在打开文件和关闭文件之间，就算本次操作
#  提示：write本身是不会换行的，要是换行只能加\n
#   写入的数据只能是字符串
#读（r）   读取文件中内容
#read() 读取文件中的所有内容，以字符串的格式显示
# readlines() 读取文件中的所有内容，以列表格式显示，列表中的每个数据，都是文件中的一行
# readline()  读取文件中的内容，每次读取一行，本身有迭代的功能    每执行一次，没结束时，是接着往下取
#追加    write()
# f=open(r'DAY1.py','a',encoding='utf-8')
# f.write('nxoewufbjdsx\n')
# f.write('文件名，权限\n')
# f.close()

# f=open(r'DAY1.py','r',encoding='utf-8')
# print(f.readline())
# print(f.readline())
# print(f.read())
# f.close()
#
# f=open(r'DAY1.py','a',encoding='utf-8')
# f.write('nxoewufbjdsx\n')
# f.write('文件名，权限\n')
# f.close()
# f=open(r'DAY1.py','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         f.write(' %d*%d=%d ' % (i,j,i*j))
#     f.write('\n')
# f.close()

# f=open(r'DAY1.py','rb')
# print(f.read())
# f.close()
#
# f=open(r'DAY1','wb')
# f.write(b'\xe4\xb8\xad\xe5\x9b\xbd\xe4\xbb\xa5\r\n')
# f.close()
#
# f=open('DAY1','w',encoding='utf-8')
# f.write('qwe')
# f.write(127)###  报错之后不会关闭文件，执行到127这句就报错   结束没有结束
# f.close()



#with语句：上下文管理器     做关闭使用    没有缩进就不在with语句中
#     作用：主动释放占用的资源
#  with语句： 两个机制   ——enter——进入、——exit——退出
#  with格式：   with  操作对象  as  变量名：
# #f=open('DAY1','w',encoding='utf-8')
# with open('DAY1','w',encoding='utf-8') as f:
#     f.write('qwe')
#     f.write('127')    # 执行with语句后会先申请enter，然后执行open后内容，执行127时报错，就自动直接关闭文件了，节省运行空间
#     f.close()

#import语句     导入语句：将其他python文件中的代码导入到本文件执行
# 格式：  import  文件名     导入这个文件的所有代码
# import 函数   #调用函数文件中的函数代码块
# print(函数.x(50))
#from 文件名 import 函数名    ：只导入文件中的某一个函数
# from DAY1 import a    #可以跟多个函数   ，*代表将文件中的函数都导入
# print(a(10))
#在Python中，类似导入文件，在Python中不叫文件，都叫做模块
#下载模块的方式
#1.pip下载：   在cmd中输入pip install 模块名
#pip出现错误，不是内部或者外部命令，是因为pip程序不在环境变量中，解决方法是将pip路径手动加入环境变量中
#   pip路径：安装Python的文件夹中的scripts   将路径复制到cmd中 D:\Python37\Scripts
#   pip是Python自带的一个下载模块的组件

#2.通过pycham安装：
# paramiko
# xlrd
# xlutils
# requests

#3.通过文件来安装，没有网络也可以安装，前提是要有文件
#     通过有网的设备，到网上下载模块 ；  有两种不同格式  （.whl）和（.tar.gz）
#     将文件传输到无网络的设备上（连网线共享、u盘）；
#     在cmd下通过命令安装  两个命令安装
# 1.。。。3.1 安装命令:pip install 文件名.whl
# （打开下载的文件的目录，按着shift，然后右键可以打开powershell进入界面接可以安装）
# 2.。。。 3.2    Python setup.py(.gz解压后的文件) install 或者是 pip install 文件名（和.whl一样）
#    在Python的官网上下载   pypi中搜索模块 最左边第三个download files

#dir 查看目录下文件
#cd.. 返回上一级目录，不能切换盘符
#  cd /d D:\（切换的盘符名称）     切换盘符


#################################异常处理语句#####################################
#异常：是因程序逻辑或者语法错误导致的程序中断
#异常处理：对将要发生的异常进行预防
#try ... except .... 语句
#      如果try里面的执行语句报错就执行except里面的执行语句
#       如果try里面的执行语句没有报错，except里面的语句就不会执行
# try:
#     a=32                   #执行语句
#     print(a+b)
# except NameError as e:      #except后很忙都不跟，默认预防所有的错误；
#                        #如果加上一个错误类型，只预防这个类型的错误
#                        #上面是固定的一个类型，下面可以跟很多个except语句
#     print(e)              #执行语句
#     print(31)
#     print

#try.....except....else....   只要不执行except语句就执行else语句
#try.....except...finally..... 无论是执行try语句，还是执行excqept语句，finally语句一定执行

# try:
#     a=32                   #执行语句
#     print(a+12)
# except NameError as e:      #except后很忙都不跟，默认预防所有的错误；
#                        #如果加上一个错误类型，只预防这个类型的错误
#                        #上面是固定的一个类型，下面可以跟很多个except语句
#     print(e)              #执行语句
# else:
#     print(31)
# finally:
#     print(83)

########################触发异常（自定义异常）#########
# raise TypeError('自己定义的异常')
# raise 是报错的异常，只要写了，无论脚本正确与否，都会报错
#
# a=int(input('>>>>'))
# if a<5:
#     raise TypeError('9283')
# else:
#     raise NameError('19374R')
# print(chr(97))   #将数字转换 为ASCII表中的字符
# print(ord('s'))     #将ASCII表中的字符转换为数字
# hex()   #十进制转十六进制
# oct()     #十进制转八进制
# bin()     #十进制转二进制
# int()     #任何人进制数转十进制








