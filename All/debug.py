#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# ----------------------------断言 assert------------------------
# 启动Python解释器时可以用-O参数来关闭assert： $ python -O err.py

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')


# ----------------------------logging（终极武器）-------------------------
import logging
# 配置logging 指定记录信息的级别 有debug，info，warning，error等
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


# ---------------------------pdb----------------------------------
# 启动 $ python -m pdb err.py
# 输入命令l来查看代码(Pdb) l  n单步执行代码(Pdb) n    p 变量名来查看变量 (Pdb) p s   q结束调试 (Pdb) q
s = '0'
n = int(s)
print(10 / n)


# -------------------------pdb.set_trace()-----------------------------
# 在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停  用(Pdb) p查看变量  用Pdb) c继续运行
print(10 / n)


