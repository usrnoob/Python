#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# file-like Object：像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object
# ------------------读文件-------------------------------
# 打开一个文件对象 'r'表示读   读取GBK编码的文件,默认UTF-8 忽略错误
f = open('/Users/michael/test.txt', 'r', encoding='gbk', errors='ignore')
f = open('/Users/michael/test.jpg', 'rb')  # 读取二进制文件 用'rb'

# 如果文件打开成功 调用read()读取文件全部内容到内存 用一个str对象表示
f.read()  # 读取所有文件
f.readline()  # 每次读取一行内容
f.readlines()  # 一次读取所有内容并按行返回list
f.read(5) # 每次最多读取5个字节的内容
f.truncate()  # 清空文件内容
# 调用close()方法关闭文件 文件使用完毕后必须关闭
f.close()

# 用with可以在文件使用完毕后正确地关闭文件
with open('/path/to/file', 'r') as f:
    print(f.read())

# ------------------------写文件------------------------------
# 'w' 表示写文本文件   'wb'表示写二进制文件  将字符串自动转换成指定编码  'a'以追加（append）模式写入到文件末尾
f = open('/Users/michael/test.txt', 'w', encoding='gbk')
f.write('Hello, world!')

# 写文件时  系统会把数据放到内存缓存起来  调用close()方法时  系统才把没有写入的数据全部写入磁盘
f.close()

# 用with可以在文件使用完毕后正确地关闭文件 写入所有数据
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')


#---------------------StringIO---------------------------
# 在内存中读写str

from io import StringIO
# 创建一个StringIO
f = StringIO()
f.write('hello')
# getvalue() 用于获得写入后的str
print(f.getvalue())

# 用一个str初始化StringIO 然后读取
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


#---------------------BytesIO---------------------------
# 在内存中读写bytes
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 用一个bytes初始化BytesIO 然后读取
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()


# ----------------------------操作文件和目录-----------------------
import os
os.name # 返回操作系统类型
os.uname() # 获取详细的系统信息
os.environ # 获取操作系统中定义的环境变量
os.environ.get('PATH') # 获取某个环境变量的值
os.path.abspath('.') # 查看当前目录的绝对路径


# os.path.join() 把两个路径合成一个
os.path.join('/Users/michael', 'testdir')  # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.mkdir('/Users/michael/testdir') # 然后创建一个目录
os.rmdir('/Users/michael/testdir') # # 删掉一个目录
os.path.split('/Users/michael/testdir/file.txt')   # os.path.split() 拆分目录
os.path.splitext('/path/to/file.txt')  # os.path.splitext()得到文件扩展名
os.rename('test.txt', 'test.py') # 对文件重命名
os.remove('test.py') # 删除文件

# 列出当前目录下的所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]

# 列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']



