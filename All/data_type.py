# Python程序是大小写敏感的
# Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，
# 而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。
# 对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向。



# --------------------------字符串-------------------------------
# 字符串是以Unicode编码  字符串是以单引号'或双引号"括起来的任意文本
# 转义字符\   \n表示换行  \t表示制表符   \\表示的字符就是\
# 可以用""把'括起来输出'  如果字符串内部既包含'又包含" 则可以用转义字符\来标识
# 'I\'m \"OK\"!'   表示的字符串内容是：  I'm "OK"!

# 用'''...'''的格式表示多行内容代替\n
print('''line1
... line2
... line3''')


# ord()函数获取字符的整数表示
ord('A')
# chr()函数把编码转换为对应的字符
chr(66)

# 把字符变为以字节为单位的bytes类型的数据
x = b'ABC'
# 计算包含的字节数
len(b'ABC')
# 计算包含的字符数
len('ABC')


# 纯英文的str可以用encode()方法用ASCII编码为bytes
'ABC'.encode('ascii')
# 含有中文的str可以用UTF-8编码为bytes
# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
# 应当始终坚持使用UTF-8编码对str和bytes进行转换。
'中文'.encode('utf-8')

# 把bytes变为str 用decode()
b'ABC'.decode('ascii')
# 把bytes变为str  在bytes中，无法显示为ASCII字符的字节，用\x##显示。
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# f-string 在字符串中包含变量
module_count = 3
print(f"本次测试覆盖了{module_count}个模块")

# 将字符串作为变量名
var = "This is a string"
varName = 'var'
s= locals()[varName]
print(s)
# -------------------格式化----------------------------
# 输出格式化的字符串用%  %s表示用字符串替换  %d表示用整数替换  %f浮点数  %x十六进制整数
# 有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
'Hi, %s, you have $%d.' % ('Michael', 1000000)

# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
'Age: %s. Gender: %s' % (25, True)

# 转义，用%%来表示一个%
'growth rate: %d %%' % 7

# 字符串的format()方法用来格式化字符串
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)

# --------------------- 整数 --------------------------
# Python的整数没有大小限制
# 1，100，-8080，0 等等
# 十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2

# ----------------------float-------------------------
# Python的浮点数没有大小限制，但是超出一定范围就直接表示为inf（无限大）
# 1.23，3.14，-9.01 等等   把10用e替代


# ----------------------布尔值-------------------------
# 布尔值可以用and、or和not运算。
True
False
3 > 2
3 > 5


# ----------------------空值-------------------------
None

# ----------------------变量-------------------------
# 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
# __xxx__ 这种是特殊变量 可以直接访问
# _name 外部可以访问 但是，请把我视为私有变量 不要随意访问
# __name 定义private变量 外部不能访问 除非用 _className__name 也可以访问
a = 1
# 同一个变量可以反复赋值，而且可以是不同类型的变量
# 这种变量本身类型不固定的语言称之为动态语言 与之对应的是静态语言（Java)
a = 123 # a是整数
a = 'ABC' # a变为字符串

# 当我们写：
a = 'ABC'
# 时，Python解释器干了两件事情：
# 1. 在内存中创建了一个'ABC'的字符串；
# 2. 在内存中创建了一个名为a的变量，并把它指向'ABC'。
# 也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如：
a = 'ABC'
b = a
a = 'XYZ'
print(b)

# ----------------------常量-------------------------
# 用全部大写的变量名表示常量
PI = 3.14159265359

# ----------------------除法/和//-------------------------
# /除法计算结果是浮点数  10 / 3 = 3.3333333333333335
# //除法计算结果是整数   10 / 3 = 3



