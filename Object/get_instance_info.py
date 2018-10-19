# -*- coding:utf-8 -*-

# ----------------------------------获取对象信息-------------------------
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# 判断对象类型
type(123)
type('str')
type(abs)
type('abc')==type('123')
type('abc')==str

# 判断一个对象是否是函数
import types

def fn():
    pass

type(fn)==types.FunctionType
type(abs)==types.BuiltinFunctionType

# 能用type()判断的基本类型也可以用isinstance()判断：
isinstance('a', str)

# 判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
isinstance([1, 2, 3], (list, tuple))

# 获得一个对象的所有属性和方法
dir('ABC')
# 返回一个包含字符串的list :
# ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
# len('ABC')='ABC'.__len__()

# 配合getattr()、setattr()以及hasattr()  操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()
hasattr(obj, 'x') # 有属性'x'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
getattr(obj, 'y') # 获取属性'y'
obj.y # 获取属性'y'
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
fn() # 调用fn()与调用obj.power()是一样的

# 如果知道对象信息 就直接写sum = obj.x + obj.y 而不是sum = getattr(obj, 'x') + getattr(obj, 'y')


#----------------------------------实例属性和类属性--------------------------
# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字

class Student(object):
    name = 'Student'
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name) # # 打印类的name属性

s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
