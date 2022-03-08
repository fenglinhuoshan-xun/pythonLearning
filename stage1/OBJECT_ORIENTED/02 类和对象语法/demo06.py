"""
    封装 -- 属性
"""

# python中的私有化的方法：用属性来实现。这个版本不是最终版
# 为了满足python面向对象中更好的观察数据

# 1. 创建实例变量（私有化实例变量）
# 2. 提供两个公开的读写方法保护实际存储数据的这个变量
# 3. 创建类变量，存储property对象


class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.set_age(age)
        self.age = age # 因为我们构造了类变量，所以没有创建实例变量，而是操作类变量，25给的是set_age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 20 <= value <= 50:
            self.__age = value # 实际存储数据的是__age，实则是_Wife__age
        else:
            raise Exception("我不要")

    # 这是个类变量，为了建立实例变量和后续相关方法之间的联系，所以类变量的名称要与实例变量的名称相同
    # property函数要写两个参数，一个读方法，一个写方法
    # property作用：拦截，将对变量的操作拦截，变成对方法的操作
    age = property(get_age, set_age)


w01 = Wife("宁宁", 25)
w02 = Wife("铁锤", 26)


# w01.set_age(27)
w01.age = 27
print(w01.age)

print(w01.__dict__) # {'name': '宁宁', '_Wife__age': 27}
