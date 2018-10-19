# ----------------------------List-----------------------------
# 一种有序的集合  查找和插入的时间随着元素的增加而增加
classmates = ['Apple', 123, True]
list(range(1, 11))  # 生成1到10的list

# 获得list元素的个数
len(classmates)
# 往list中追加元素到末尾
classmates.append('Adam')
# 把元素插入到索引号为1的位置
classmates.insert(1, 'Jack')
# 删除list末尾的元素  删除指定位置的元素，用pop(i)
classmates.pop()
# 把某个元素替换成别的元素
classmates[1] = 'Sarah'
# 二维数组 要拿到'php'可以写p[1]或者s[2][1]
s = ['python', 'java', ['asp', 'php'], 'scheme']
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']

# ----------------------List Comprehensions  列表生成式----------------------
# 可以用来创建list的生成式

# 生成[1x1, 2x2, 3x3, ..., 10x10]
[x * x for x in range(1, 11)]

# 加上if筛选出仅偶数的平方
[x * x for x in range(1, 11) if x % 2 == 0]

# 使用两层循环，可以生成全排列
[m + n for m in 'ABC' for n in 'XYZ']

# 列出当前目录下的所有文件和目录名
import os  # 导入os模块，模块的概念后面讲到

[d for d in os.listdir('.')]  # os.listdir可以列出文件和目录

# 列表生成式使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
[k + '=' + v for k, v in d.items()]

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

# -----------------------------生成器：generator---------------------
# 不必创建完整的list 在循环的过程中不断推算出后续的元素 从而节省大量的空间
# 把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))

# 获得generator的下一个值 这种方法不推荐
next(g)

# 推荐用迭代
for n in g:
    print(n)

# 生成斐波拉契数列：除第一个和第二个数外，任意一个数都可由前两个数相加得到
# 普通函数 顺序执行，遇到return语句或者最后一行函数语句就返回
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(6) #以输出斐波那契数列的前6个数


# 把fib函数变成generator 用yield关键字替换掉print(b)
# generator函数 遇到yield语句返回 再次执行时从上次返回的yield语句处继续执行
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 执行到 yield b 时，fab 函数就返回一个迭代值
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in fib(6):
    print(n)


# ----------------------------tuple--------------------------------
# 一旦初始化就不能修改 是说指向永远不变 list['A', 'B'] 里的内容可以改变
t = ('a', 'b', ['A', 'B'])
# 只有1个元素的tuple定义
t = (1,)
