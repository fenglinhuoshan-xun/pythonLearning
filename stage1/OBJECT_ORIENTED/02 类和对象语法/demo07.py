"""
    封装 -- 标准属性
        作用：保护实例变量，保护的本质就是拦截的思想，将对变量的操作变成对属性的操作
"""


# python中的私有化的方法：用属性来实现
# 最终版本：实例变量和相关方法之间的联系，我们就不要用类变量去实现了，用@property来实现

# 标准属性创建步骤：
# 1. 创建实例变量（私有化实例变量）
# 2. 提供两个公开的读写方法保护实际存储数据的这个变量
# 3. 使用@property修饰读取方法
#    使用@属性名.setter修饰写入方法

# 属性本质就是那两个读写方法

class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.set_age(age)
        self.age = age

    @property  # 创建property对象，自动绑定下面这个方法（读方法），作为第一个参数
    def age(self):  # 下面这个方法如果叫get_age，好比我们的类变量叫get_age，那就和实例变量没有关系了，所以要求方法名必须和实例变量名称相同
        return self.__age

    @age.setter  # @age，相当于那个类变量，存储的是property对象的地址，.setter就是将下面这个方法（写方法）传到这个对象的第二个参数上
    # 自动绑定下面的方法（写入）
    def age(self, value):
        if 20 <= value <= 50:
            self.__age = value  # 实际存储数据的是__age，实则是_Wife__age
        else:
            raise Exception("我不要")

    # age = property(get_age, set_age)


w01 = Wife("宁宁", 25)
w02 = Wife("铁锤", 26)

# w01.set_age(27)
w01.age = 27
print(w01.age)

print(w01.__dict__)  # {'name': '宁宁', '_Wife__age': 27}
