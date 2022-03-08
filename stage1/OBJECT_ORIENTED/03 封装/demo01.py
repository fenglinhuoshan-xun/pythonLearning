"""
    封装 -- 设计思想
        请以面向对象的思想，描述一下情景:
            老张开车去东北
"""


# 我们拿到一个需求，该怎么去思考呢？我们要思考，哪些事物具有行为
# 因为我们在做封装时，分而治之，变则疏之，主要就是考察行为上的变化
# 这里面就两个事物，老张有开车的行为，车有驮着老张去的行为，即有行驶的行为
# 写法1：每次都会创建一辆新车
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, pos):
        print("去", pos)
        # 要调用别的类的实例方法，则需要创建别的类的对象，通过对象去调用
        # 创建对象如果写在go_to方法中，则表示，每次调用这个方法，每次去一个地方时，都会创建一辆新车
        car = Car()
        car.run()


class Car:
    def run(self):
        print("嘟嘟嘟...")


lz = Person("老张")
lz.go_to("东北")


# 写法2：老张的车
class Person:
    def __init__(self, name=""):
        self.name = name
        # 将创建车的代码放到构造函数中完成，表示创建自己的车，因为构造函数开辟完栈帧后会释放，为了持久化保存自己的车，所有要加self，创建了一个实例变量
        # 创建人的时候，有了一辆车
        self.car = Car()

    def go_to(self, pos):
        print("去", pos)
        # 调用的时候，也用self去点
        self.car.run()


class Car:
    def run(self):
        print("嘟嘟嘟...")


lz = Person("老张")
lz.go_to("东北")
lz.go_to("西北")


# 写法3：人与车的关系松散，人去一个地方不一定要车，可以用其他工具
class Person:
    def __init__(self, name=""):
        self.name = name

    # 如果老张不是开车去东北，而是开飞机呢？也就是说我们去哪这个事可能会用多种交通工具
    # 那么我们就不能把它写死，我们可以将交通工具作为参数传给方法，调的时候，直接用参数去调就行
    def go_to(self, pos, vehicle):
        print("去", pos)
        vehicle.run()


class Car:
    def run(self):
        print("嘟嘟嘟...")


lz = Person("老张")
# 在类外创建对象，作为参数传给方法
c01 = Car()
lz.go_to("东北", c01)
lz.go_to("西北")
