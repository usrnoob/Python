# ---------------------------------dict--------------------------------
# Dictionary （key-value）（类似java中的map） 具有极快的查找和插入速度
# dict的key必须是不可变的 所以不重复 不可以放入可变对象（比如list）
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 把数据放入dict
d['Adam'] = 67

# 通过in判断key是否存在1.
'Thomas' in d
# 通过in判断key是否存在2. 如果key不存在，可以返回None，或者自己指定的value
d.get('Thomas', -1)

# 删除一个key 用pop(key)
d.pop('Bob')

# 遍历dict
for key, value in d.items():
    print(key, value)

# Like Switch Case
def pickNum(number):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(number, "nothing")
print(pickNum(1))

# -------------------------------------Set-------------------------------
# Set 无序不重复元素的序列  不可以放入可变对象（比如list）
s = set([1, 2, 3])
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# add(key)方法可以添加元素到set中
s.add(4)
# remove(key)方法可以删除元素
s.remove(4)

