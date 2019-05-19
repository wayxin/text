#! /usr/bin/python
# -*- coding:utf-8 -*-
# splb=[
#     {"name":"电脑","price":2000},
#     {"name":"鼠标","price":100},
#     {"name":"游艇","price":5000},
#     {"name":"美女","price":6000},
#     {"name":"空无","price":0}
# ]
# a=int(input('请输入银行卡金额:'))
# b=[]
# c=[]
# while True:
#     print('商品列表')
#     for i,j in enumerate(splb):
#         print(i,j)
#     d=int(input('请选择商品:'))
#     if d>4 or d<0:
#         print('没有该商品')
#         break
#     else:
#         s=splb[d]
#         b.append(s)
#         print('购物车:')
#         print(b)
#         c.append(splb[d]['price'])
#         u=sum(c)
#         print('价格{}'.format(u))
#     e=int(input('请输入选择:1.结算2.删除商品3.充值4.退出5.继续添加:'))
#     if e==1:
#         if a>u or a==u:
#             print('购买成功')
#             a=a-u
#             c.clear()
#             b.clear()
#             print('余额为{}'.format(a))
#         if a<u:
#             print('购买当前商品余额不足，请充值,或退出')
#             h=u-a
#             print('需充值{}元'.format(h))
#             i=int(input('请选择:1.充值2.退出3.删除商品'))
#             if i==1:
#                 g = input('请输入充值金额:')
#                 a = int(a) + int(g)
#                 print('当前余额{}元'.format(a))
#             if i==2:
#                continue
#             if i==3:
#                 for i, j in enumerate(splb):
#                     print(i, j)
#                 print(b)
#                 h = int(input('请输要删除的商品号:'))
#                 c.remove(splb[h]['price'])
#                 b.remove(splb[h])
#                 print(c)
#                 print(b)
#     if e==2:
#          for i, j in enumerate(splb):
#             print(i, j)
#          print(b)
#          h=int(input('请输要删除的商品号:'))
#          c.remove(splb[h]['price'])
#          b.remove(splb[h])
#          print(c)
#          print(b)
#     if e==3:
#         g = input('请输入充值金额:')
#         a = int(a) + int(g)
#         print('当前余额{}元'.format(a))
#     if e==4:
#         print('再见')
#         break