#! /usr/bin/python
#- -*- coding:utf-8 -*-
import unittest
from jiekou_kuangjia.config.bingli_xinxi import bingli

class bbl(unittest.TestCase):
    bl=bingli().bl
    def test_yi(self):
        self.assertEqual(self.bl()['code'],0)
        self.assertEqual(self.bl()['data']['diseaseHistory'][0]['guid'],'159d96e3-25f0-11e9-a4d7-0242ac120003')
    def test_er(self):
        self.assertNotEqual(self.bl()['code'],0)
if __name__ == '__main__':
    unittest.main()