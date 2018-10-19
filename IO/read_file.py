# -*- coding:utf-8 -*-

# ------------------Read file----------------------
# 用命令行参数的方式读取文件内容 $python read_case.py tt.txt
from sys import argv

script, file_path = argv

print(f"读取文件: {file_path}")
print()
file_obj = open(file_path)
print(file_obj.read())
file_obj.close()


