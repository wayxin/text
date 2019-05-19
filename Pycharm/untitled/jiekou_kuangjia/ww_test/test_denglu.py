

import unittest
from jiekou_kuangjia.config.qingqiu import wind
from jiekou_kuangjia.data.duqu import shuju

class win(unittest.TestCase):
    bb=wind().denglu
    aa=shuju()
    def test_1(self):
        qq = self.bb(int(self.aa[0][0]), int(self.aa[0][1]))
        self.assertEqual(qq['code'], 0)
        self.assertEqual(qq['msg'], 'OK')
    def test_2(self):
        for j in range(1,len(self.aa)):
            ww = self.bb(int(self.aa[j][0]), int(self.aa[j][1]))
            self.assertNotEqual(ww['code'], 0)
            self.assertNotEqual(ww['msg'], 'OK')
if __name__ == '__main__':
    unittest.main()