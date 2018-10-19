# -*- coding:utf-8 -*-

# ------------------Write file----------------------
# $ python write_case.py 002 Get接口测试 接口返回的状态码必须是200
# 这时候当前文件夹会出现case002.txt文件
from sys import argv

script, case_number, case_name, assertion = argv

file_name = 'case002.txt'

print(f"用例编号: {case_number}")
print(f"用例名称: {case_name}")
print(f"断言: {assertion}")

target = open(file_name, 'w')

print("Truncating the file. Goodbye!")

print(f"write file: {file_name}")

target.write(f"用例编号: {case_number}")
target.write("\n")
target.write(f"用例名称: {case_name}")
target.write("\n")
target.write(f"断言: {assertion}")
target.write("\n")
target.close()