#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# --------------------------------序列化----------------------------
# 在程序运行的过程中，所有的变量都是在内存中 一旦程序结束，变量所占用的内存就被操作系统全部回收
# 把变量从内存中变成可存储或传输的过程称之为序列化
# 在Python中叫pickling  使用pickle模块       在Java中叫serialization

# 把一个对象序列化并写入文件
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d) # pickle.dumps()方法把任意对象序列化成一个bytes

# 用pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()


# 把对象从磁盘读到内存 先把内容读到一个bytes  然后用pickle.loads()方法反序列化出对象
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
