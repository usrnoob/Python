# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。

# 定义函数时，需要确定函数名和参数个数；
#
# 如果有必要，可以先对参数的数据类型做检查；
#
# 函数体内部可以用return随时返回函数结果；
#
# 函数执行完毕也没有return语句时，自动return None。
#
# 函数可以同时返回多个值，但其实就是一个tuple。

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))


#---------------------------空函数pass--------------------------
# 空函数  先放一个pass，让代码能运行起来。
def nop():
    pass
# pass还可以用在其他语句里，比如：
age = 8
if age >= 18:
    pass

# --------------------------参数检查----------------------------
# 参数个数不对，Python会抛出TypeError
# 参数类型不对 要自定义参数类型检查, 数据类型检查可以用内置函数isinstance()实现
# 这里只允许整数和浮点数类型的参数
def you_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# --------------------------返回多个值----------------------------
# Python的函数返回多值其实就是返回一个tuple  而多个变量可以同时接收一个tuple，按位置赋给对应的值
import math  # 导入math包
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)
print(x, y)
print(r)

# --------------------------参数----------------------------
# 必选参数在前，默认参数在后
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

power(5)

# 默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数*  允许传入0个或任意个参数  在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 关键字参数**  允许传入0个或任意个含参数名的参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


#命名关键字参数


#递归函数

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


