# -*- coding:utf-8 -*-
# 用input()函数来获取用户输入的信息，并保存在变量里。

case_name = input("请输入用例名称:\n")
test_data = input("请输入用到的测试数据，比如: 测试站点=www.itest.info:\n")
test_steps = input("请输入测试步骤:\n")
test_assert = input("请输入测试断言(预期结果):\n")

formatter = """
用例名称: {}
测试数据: {}
测试步骤: {}
测试断言: {}
"""

print(formatter.format(case_name, test_data, test_steps, test_assert))
