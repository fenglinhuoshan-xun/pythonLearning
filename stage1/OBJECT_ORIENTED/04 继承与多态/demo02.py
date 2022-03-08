"""
    继承 -- 数据
"""


class Person:
    def __init__(self, name=""):
        self.name = name


class Student(Person):
    def __init__(self, name="", score=0):  # 构造函数的参数中，也要有父类的构造函数的参数
        super().__init__(name)  # 要想使用父类数据，必须要调用父类数据，用super()去调，因为调用父类构造函数需要一个name参数，所有我们传入一个name参数
        # self.name = name # 我们也可以直接将父类数据拿过来即可，开发过程中，不可能这么做，因为父类数据可能很多
        self.score = score


# 如果子类没有构造函数，直接使用父类构造函数
s01 = Student("悟空", 100)
print(s01.name)
