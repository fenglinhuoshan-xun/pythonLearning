"""
    属性 -- 常见写法
"""


# 1. 读写属性
class Wife01:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):  # 秘书
        return self.__age  # 老板

    @age.setter
    def age(self, v):
        self.__age = v


# 在python中，自己调用自己叫递归，递归是有最大深度的

w01 = Wife01(25)
print(w01.age)
print(w01.__dict__)


# 2. 只读属性
class Wife02:
    def __init__(self):
        self.__age = 26

    @property
    def age(self):  # 秘书
        return self.__age  # 老板


w01 = Wife02()
print(w01.age)
# w01.age = 100 # 不能写入
print(w01.__dict__)


# 3. 只写属性
class Wife03:
    def __init__(self, age=0):
        self.age = age

    # @age.setter
    def __set_age(self, v):
        self.__age = v

    age = property(None, __set_age)


# 可以写
w01 = Wife03(25)
# 可以改
w01.age = 26
# 不能读
# print(w01.age)
print(w01.__dict__) # {'_Wife03__age': 26}
