# for循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# range(5)生成从0开始小于5的整数   list()函数可以转换为list
list(range(5))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while 循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break 结束当前循环
# continue 跳过当前的这次循环，直接开始下一次循环。
