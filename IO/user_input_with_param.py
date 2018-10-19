# -*- coding:utf-8 -*-
# ------------------------命令行参数--------------------------------
# 在命令行中使用下面的命令去执行代码 $python gen_test_case_with_id.py itest_001
# itest_001 是传入的参数 不然会报错
# 在 Pycharm Run configuration里加入这个参数

# argv的意思是argument variable  argv里保存了脚本运行时你传入的所有的命令行参数以及脚本名称
# 例如
# python something.py first second third # argv = [something.py, first, second, third]
# python something.py my_var # argv = [something.py, my_var]
# python something.py # argv = [something.py]

# -----------------------unpack------------------------
# unpack就是把一组数据按顺序的保存到变量里
# argv = ['something.py', 'first', 'second', 'third']
# a, b, c, d = argv  # a='something.py' b='first', c=second d='third'
#
# argv = ['something.py', 'my_var']
# script, the_var = argv  # script='something.py' the_var='my_var'


from sys import argv

# script, case_id = argv的作用就是把第1个命令行参数赋值给变量case_id
script, case_id = argv
print(f"创建测试用例\n用例编号: {case_id}")
case_name = input("请输入用例名称:\n")
test_data = input("请输入用到的测试数据，比如: 测试站点=www.itest.info:\n")
test_steps = input("请输入测试步骤:\n")
test_assert = input("请输入测试断言(预期结果):\n")

formatter = """
用例编号: {}
用例名称: {}
测试数据: {}
测试步骤: {}
测试断言: {}
"""

print(formatter.format(case_id, case_name, test_data, test_steps, test_assert))



# -----------------------
# 需要模块：sys
# 参数个数：len(sys.argv)
# 脚本名：    sys.argv[0]
# 参数1：     sys.argv[1]
# 参数2：     sys.argv[2]

import sys

print
"脚本名：", sys.argv[0]
for i in range(1, len(sys.argv)):
    print
    "参数", i, sys.argv[i]

# >>>python test.py hello world
# 脚本名：test.py
# 参数 1 hello
# 参数 2 world
