#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

# 通过属性来访问
d = Dict(a=1, b=2)
d['a']
d.a


