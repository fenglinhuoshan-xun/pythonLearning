"""
    继承 -- 方法
        财产上的继承：钱不用孩子挣，但是可以花
        皇位上的继承：江山不用太子打，但是可以坐
        代码上的继承：子类不用写那个代码，但是可以直接用
"""


# 当我们在程序当中发现，有多个类有相同代码的时候，且这多个类在概念上是统一的，我们就要将概念统一
# 在概念上统一：指两个类，都属于是一种什么，这个什么就是他们俩的那个概念。学生和老师都属于人，所有说人是他们俩统一的概念

class Person:
    def say(self):
        print("说话")


# 此时Student就叫做子类，Person就叫做父类，我们可以继承多个父类，即写多个父类参数
class Student(Person):
    def study(self):
        print("学习")
        # 可以当成是自己的，直接用self调用，但不建议，因为数据多了容易混淆到底是自己的，还是继承而来的
        # self.say()
        # 建议通过super()去点，即就是用父类对象去点父类方法
        super().say()  # 说白了，其实super()这个东西还是本类的，只是通过这个关键字可以访问到父类的东西。父类也可以叫做超类


class Teacher(Person):
    def teach(self):
        print("教学")


p01 = Person()
# 父类对象，只能访问父类成员
p01.say()

s01 = Student()
# 子类对象，可以访问父类成员和本类成员
# 我们可以在这个类的外面直接去用
s01.say()
s01.study()

t01 = Teacher()
# 不能访问兄弟类成员
# t01.study()


# 跟继承相关的内置函数
# 1. isinstance：判断一个对象是不是一种类型，是返回True，不是返回False

# 人对象 是一种 人类型
print(isinstance(p01, Person))  # True
# 学生对象 是一种 人类型
print(isinstance(s01, Person))  # True
# 老师对象 是一种 学生类型
print(isinstance(t01, Student))  # False
# 人对象 是一种 老师类型
print(isinstance(p01, Teacher))  # False

# 2. issubclass：判断一个类型是不是一个类型，是返回True，不是返回False

# 人类型 是一种 人类型
print(issubclass(Person, Person))  # True
# 学生类型 是一种 人类型
print(issubclass(Student, Person))  # True
# 老师类型 是一种 学生类型
print(issubclass(Person, Student))  # False
# 人类型 是一种 老师类型
print(issubclass(Person, Teacher))  # False

# 3. type：判断一个对象的类型是不是这个类型，必须完全是本类型才返回True，否则返回False

# 人对象 是 人类型
print(type(p01) == Person)  # True
# 学生对象 是 人类型
print(type(s01) == Person)  # False
# 老师对象 是 学生类型
print(type(t01) == Student)  # False
# 人对象 是 老师类型
print(type(p01) == Teacher)  # False
