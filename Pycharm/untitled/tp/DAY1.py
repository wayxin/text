
# print('119')
#
# a=lambda x:x+2
#
# def x(a):
#     b=0
#     for i in range(a+1):
#         b=i+b
#     # print(b)
#     return  b
#
# if __name__ == '__main__':    #判断执行的文件是否是执行语句所在的文件
#     print('110')
# #__name__:函数   获取当前执行的文件名







# user=int(input('请输入总资产：'))
# a=[
#     {'name':'电脑','price':1999},
#     {'name':'鼠标','price':10},
#     {'name':'游艇','price':20},
#     {'name':'美女','price':998}
# ]
# print('商品单')
# def n(n):
#     for i,j in enumerate(n):
#         print(i+1,j)
# n(a)
# car=[]
# while True:
#     i=int(input('请输入商品序号，购买请输入负数：'))
#     if i>len(a):
#        i=int(input('请输入商品序号，购买请输入负数：'))
#     if i>len(a):
#         i=int(input('请输入商品序号，购买请输入负数：'))
#     if i>len(a):
#         i=int(input('请输入商品序号，购买请输入负数：'))
#     if i<0:
#         break
#     print('已加入商品{}'.format(a[i-1]))
#     car.append(a[i-1])
#     print('购物车商品单')
#     n(car)
#     f=len(car)
#     num,c,d=0,0,0
#     for e in range(0,f):
#         b=car[num]['price']
#         c=c+b
#         num=num+1
#     print('购物车商品总金额为：{}'.format(c))
#     i=i+1
# if c>user:
#        print('账户余额不足,请充值1，或删除购物车商品2')
#        chongzhi=int(input('更改码1充值，2删除:'))
#        if chongzhi==1:
#            l=(c-user)
#            user1=int(input('请填写充值金额{}：'.format(l)))
#            b=(user1+user)
#        if b>=c:
#            print('购买成功')
#        if chongzhi==2:
#            print('购物车商品单')
#            n(car)
#            k=int(input('请输入要删除的商品号：'))
#            car.pop(k-1)
#            print(car)
#            p=len(car)
#            q=0
#            for z in range(0,p):
#                o=car[z]['price']
#                q+=o
#            if user>=q:
#                print('购买成功')
# else:
#     print('购买成功')








#!/usr/bin/python
#-*- coding:utf-8 -*-
# while True:
#     try:
#         user=int(input('请输入总资产：'))
#         if user<0:
#             raise TypeError('user')
#     except:
#         print('输入错误，请重新开始购买')
#         break
#     else:
#         print('输入成功')
#         a=[{'name':'电脑','price':1999},{'name':'鼠标','price':10},{'name':'游艇','price':20},{'name':'美女','price':998}]
#         print('商品单')
#         def n(n):
#             for i,j in enumerate(n):
#                 print(i+1,j)
#         n(a)
#         car=[]
#         while True:
#             for z in range(1,4):
#                 i=int(input('请输入商品序号，购买请输入0：'))
#                 if i>len(a) or i<0:
#                     print('请重新输入还剩{}次机会'.format(4-z-1))
#                     continue
#                 if i<=len(a):
#                     break
#                 if i==0:
#                     break
#             print('已加入商品{}'.format(a[i-1]))
#             car.append(a[i-1])
#             print('购物车商品单')
#             n(car)
#             f=len(car)
#             num,c,d=0,0,0
#             for e in range(0,f):
#                 b=car[num]['price']
#                 c=c+b
#                 num=num+1
#             print('购物车商品总金额为：{}，余额为：{}'.format(c,(user-c)))
#             i=i+1
#             try:
#                 if c>user:
#                    print('账户余额不足,充值输入1，或删除购物车商品输入2')
#                    chongzhi=int(input('更改码1充值，2删除:'))
#                    if chongzhi==1:
#                        h=0
#                        while True:
#                            user1=int(input('请填写充值金额{}：'.format((c-user))))
#                            h+=user1
#                            # print('还得充值{}'.format((c-user)-h))
#                            b=(h+user)
#                            if b>=c:
#                                 print('购买成功,您的余额为{},可以继续购买'.format(b-c))
#                                 break
#                    if chongzhi==2:
#                        while True:
#                            print('您的购物车商品单')
#                            n(car)
#                            k=int(input('请输入您要删除的商品号：'))
#                            car.pop(k-1)
#                            print('您的购物车商品单')
#                            n(car)
#                            q=0
#                            for z in range(0,len(car)):
#                                o=car[z]['price']
#                                q+=o
#                            if user>=q:
#                                break
#                            if user<q:
#                                print('您的购物车金额为{}'.format(q))
#                        if user>=q:
#                             print('购买成功,您的余额为{}，可以继续购物'.format(user-q))
#                 else:
#                     print('购买成功,您的余额为{}，可以继续购物'.format(user-c))
#             except:
#                 print('购物失败，请重新开始购物')














while True:
    try:
        user=int(input('请输入总资产：'))
        if user<0:
            raise TypeError('user')
    except:
        print('输入错误，请重新开始购买')
        break
    else:
        print('输入成功')
        a=[{'name':'电脑','price':1999},{'name':'鼠标','price':10},{'name':'游艇','price':20},{'name':'美女','price':998}]
        print('商品单')
        def n(n):
            for i,j in enumerate(n):
                print(i+1,j)
        n(a)
        car=[]
        while True:
            for z in range(1,4):
                i=int(input('请输入商品序号，购买请输入0：'))
                if i>len(a) or i<0:
                    print('请重新输入还剩{}次机会'.format(4-z-1))
                    continue
                if i<=len(a):
                    break
            if i==0:
                break
            print('已加入商品{}'.format(a[i-1]))
            car.append(a[i-1])
            print('购物车商品单')
            n(car)
            f=len(car)
            num,c,d=0,0,0
            for e in range(0,f):
                b=car[num]['price']
                c=c+b
                num=num+1
            print('购物车商品总金额为：{}，余额为：{}'.format(c,(user-c)))
            i=i+1
        try:
            if c>user:
               print('账户余额不足,充值输入1，或删除购物车商品输入2')
               chongzhi=int(input('更改码1充值，2删除:'))
               if chongzhi==1:
                    h=0
                    while True:
                        user1=int(input('请填写充值金额{}：'.format((c-user))))
                        h+=user1
                        print('还得充值{}'.format((c-user)-h))
                        b=(h+user)
                        if b>=c:
                            print('购买成功,您的余额为{},可以继续购买'.format(b-c))
                            break
                if chongzhi==2:
                   while True:
                           print('您的购物车商品单')
                           n(car)
                           k=int(input('请输入您要删除的商品号：'))
                           car.pop(k-1)
                           print('您的购物车商品单')
                           n(car)
                           q=0
                           for z in range(0,len(car)):
                               o=car[z]['price']
                               q+=o
                           if user>=q:
                               break
                           if user<q:
                               print('您的购物车金额为{}'.format(q))
                       if user>=q:
                            print('购买成功,您的余额为{}，可以继续购物'.format(user-q))
            else:
                print('购买成功,您的余额为{}，可以继续购物'.format(user-c))
        except:
            print('购物失败，请重新开始购物')