#!/usr/bin/python
#-*- coding:utf-8 -*-
import unittest
from jiekou_kuang.config.qingqiu import jiekou_qingqiu
from jiekou_kuang.data.duqu import Shuju

class qwe(unittest.TestCase):
    denglu = jiekou_qingqiu().denglu
    shuju = Shuju().shuju()

    def test_qw(self):
        qq = self.denglu(int(self.shuju[0][0]),int(self.shuju[0][1]))
        self.assertEqual(qq['code'],0)
        self.assertEqual(qq['msg'],'OK')

    def test_ww(self):
        for i in range(1,len(self.shuju)):
            ww = self.denglu(int(self.shuju[i][0]),int(self.shuju[i][1]))
            self.assertNotEqual(ww['code'],0)

if __name__ == '__main__':
    unittest.main()