# ------------------------------定义类 创建实例-----------------------------
# (object)表示该类是从哪个类继承下来的
class Student(object):

    # 用特殊方法__init__绑定属性name，score
    # 第一个参数永远是实例变量self self表示创建的实例本身 不需要传
    def __init__(self, name, score):
        # __ 定义private变量 外部不能访问 Python解释器对外把__name变量改成了_Student__name
        # 外部用 _Student__name 也可以访问
        self.__name = name
        self.score = score

    # 定义一个类属性  所有实例都可以访问到
    id = 'Student'

    # 定义类的方法  第一个参数是self   封装
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    # 用来给外部代码获取name和score
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 用来给外部代码修改score
    def set_score(self, score):
        self.__score = score


# 创建实例
bart = Student('Bart Simpson', 59)
# 给实例bart绑定一个age属性
bart.age = 15
# 调用方法
bart.print_score()
print(bart.name, bart.get_grade())

# 操作类属性
print(bart.id) # 打印id属性，因为实例并没有id属性，所以会继续查找class的id属性
print(Student.id) # 打印类的id属性
bart.id = 5 # 给实例绑定id属性
print(bart.id) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的id属性
print(Student.id) # 但是类属性并未消失，用Student.id仍然可以访问
del bart.id # 如果删除实例的id属性
print(bart.id) # 再次调用bart.id，由于实例的id属性没有找到，类的id属性就显示出来了
# 所以不要对实例属性和类属性使用相同的名字




