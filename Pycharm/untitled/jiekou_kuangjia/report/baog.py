from app.testcase import HTMLTestRunner
import unittest

def baogao(name):
    suit=unittest.TestSuite()
    # suit.addTest(win('test_1'))
    # suit.addTest(win('test_2'))
    #能够接受两个参数，
    for j in name:
        dis=unittest.defaultTestLoader.discover(r'H:\PycharmProjects\untitled\jiekou_kuangjia\ww_test',pattern='test_{}.py'.format(j.strip()))
        for i in dis:
            suit.addTest(i)
    f=open('abc.html','wb')
    runner= HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='王玉鑫', description='结果如下:')
    runner.run(suit)
    f.close()
# baogao()
if __name__=='__mian__':
    pass