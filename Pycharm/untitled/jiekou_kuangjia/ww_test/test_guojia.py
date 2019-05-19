#! /usr/bin/python
#- -*- coding:utf-8 -*-
import unittest
from jiekou_kuangjia.config.guojia_xinxi import guojia

class gg(unittest.TestCase):
    gj = guojia().gj
    def test_a(self):
        self.assertEqual(self.gj()['code'], 0)
        # self.assertEqual(self.gj()['data']['A'][0]['guid'],"2fddb82c-25f2-11e9-a4d7-0242ac120003")

    def test_b(self):
        self.assertNotEqual(self.gj()['code'], 0)
        self.assertNotEqual(self.gj()['data']['A'][0]['guid'],"2fddb82c-25f2-11e9-a4d7-0242ac120003")

if __name__ == '__main__':
    unittest.main()