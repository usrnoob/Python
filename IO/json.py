#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# --------------------------------JSON---------------------------------
# JSON和Python内置的数据类型对应如下:

# JSON类型	        Python类型
# {}	            dict
# []	            list
# "string"	        str
# 1234.56	        int或float
# true/false	    True/False
# null	            None

# 把Python对象变成一个JSON
import json
d = dict(name='Bob', age=20, score=88)

# dumps()方法返回一个str 内容就是标准的JSON
# dump()方法可以直接把JSON写入一个file-like Object
json.dumps(d)

# 把JSON反序列化为Python对象  用loads()  load()方法从file-like Object中读取字符串并反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)


# Python的dict对象可以直接序列化为JSON的{}
import json
# 定义一个student类
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)

# class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
# 可选参数default=就是把任意一个对象变成一个可序列为JSON的对象
# 把任意class的实例变为dict
print(json.dumps(s, default=lambda obj: obj.__dict__))


# 把dict转换为Student实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

# 把JSON反序列化为一个Student对象实例
# loads()方法首先转换出一个dict对象   object_hook函数负责把dict转换为Student实例
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))  # 打印出的是反序列化的Student实例对象


# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
