# if else 从上往下判断 如果判断是True 则忽略掉剩下的elif和else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# input()读取用户的输入
s = input('birth: ')
# 转换为int
birth = int(s)


