# -*-coding：UTF:8-*-
import unittest


class TestMethod(unittest.TestCase):
    # 每次执行用例前执行setUp(),可以在这里做一些初始化工作
    @classmethod
    def setUp(cls):
        print('setUp')

    # 每次执行用例后执行teardown
    @classmethod
    def tearDown(cls):
        print('tearDown')

    def test001(self):  # unittest中的用例必须以test开头
        print('test001')

    def test002(self):
        print('test002')


if __name__ == '__main__':
    unittest.main()

