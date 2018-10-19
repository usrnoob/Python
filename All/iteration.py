#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型

# ------------------------------迭代------------------------------

d = {'a': 1, 'b': 2, 'c': 3}
# dict默认迭代key
for key in d:
    print(key)

# 迭代value
for value in d.values():
    pass

# 同时迭代key和value
for k, v in d.items():
    pass

# 判断一个对象是否是Iterable可迭代对象
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
isinstance([1,2,3], Iterable) # list是否可迭代
isinstance(123, Iterable) # 整数是否可迭代

# enumerate()函数把一个list变成索引-元素对  这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 迭代两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


# ----------------------------------迭代器--------------------------------
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# Iterator对象表示的是一个数据流 不能提前知道序列的长度

# 用isinstance()判断一个对象是否是Iterator迭代器对象
from collections import Iterator
isinstance('abc', Iterator)

# 把Iterable变成Iterator可以使用iter()函数
isinstance(iter('abc'), Iterator)


# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass
#实际上完全等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break