#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 遇到错误执行except finally 一定会被执行  没有错误发生会自动执行else语句
# Python所有的错误类型都继承自BaseException

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# 函数main()调用bar()，bar()调用foo()   在main()就可以捕获所有了
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

# 记录错误 用logging
# 出错程序打印完错误信息后会继续执行，并正常退出：
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')


# 抛出错误 用raise
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')

# raise语句如果不带参数，就会把当前错误原样抛出
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise