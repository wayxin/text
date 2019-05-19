#! /usr/bin/python
#- -*- coding:utf-8 -*-
import unittest
from jiekou_kuangjia.data.xinx_duqu import xx
from jiekou_kuangjia.config.geren_xinxi import grxx

class eren(unittest.TestCase):
    jiekou=grxx().geren
    shuju=xx()
    def test_one(self):
        one=self.jiekou(self.shuju[0][0],self.shuju[0][1])
        self.assertEqual(one['code'],0)
    def test_tuo(self):
        for k in range(1,len(self.shuju)):
            tuo=self.jiekou(self.shuju[1][0],self.shuju[1][1])
            self.assertNotEqual(tuo['msg'],'K')
if __name__ == '__main__':
    unittest.main()
