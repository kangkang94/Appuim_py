#coding=utf-8
import unittest
import threading
class CaseTest(unittest.TestCase):

    def setUp(self):
        print('this is setup')
    def tearDown(self):
        print('this is tearDown')

    def test_00(self):
        print('this is test_00')

        flag = False
        self.assertEqual(1,1,'数据错误')
        #self.assertEqual(1,2,'数据错误')
        self.assertFalse(flag)

    def test_01(self):
        print('this is test_01')

    @classmethod
    def setUpClass(cls):
        print('this is class')


def get_suit(i):
    print(str(i)+'hello')
    suite = unittest.TestSuite()
    suite.addTest(CaseTest('test_01'))
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    threads = []
    for i in range(3):
        print(str(i))
        t = threading.Thread(target=get_suit,args=(i,))
        threads.append(t)

    for j in threads:
        j.start()
