#!/usr/bin/env python3
# -*- coding:utf-8 -*-



import unittest

from my_dict import Dict

class TestDict(unittest.TestCase):

    # 以test开头的方法就是测试方法
    def test_init(self):
        d = Dict(a=1, b='test')
        # 断言assertEqual() 断言函数返回的结果与1相等
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        # 断言抛出指定类型的Error
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 运行单元测试
# 1.把mydict_test.py当做正常的python脚本运行
if __name__ == '__main__':
    unittest.main()

# 2.在命令行通过参数-m unittest 直接运行 (推荐）
# $ python -m unittest mydict_test


# setUp与tearDown  这两个方法会分别在每调用一个测试方法的前后分别被执行。
# 比如测试需要启动一个数据库   可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库
class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')