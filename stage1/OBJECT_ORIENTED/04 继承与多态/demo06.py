"""
    设计思想
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle):
        print("走喽")
        if not isinstance(vehicle, Vehicle):  # 如果加个判断，则继承了的数据不影响，没有继承的会报错，建议继承
            raise Exception("传入的必须是交通工具")
        vehicle.transport()


class Vehicle:
    """
        交通工具：隔离人与具体交通工具的变化
    """

    def transport(self):
        pass


# -----------------------------------------
class Car(Vehicle):
    def transport(self):
        print("嘟嘟嘟~")


# ctrl + o：可以调出所有可以重写的方法
class Airplane(Vehicle):

    def transport(self):
        print("嗖嗖嗖～")


# 网上经常说python不继承也可以，小鸭子原则：不继承也行，只要你有这个方法就可以
# 但继承相当于立法保障
# class Car():
#     def transport(self):
#         print("嘟嘟嘟~")
#
#
# class Airplane():
#
#     def transport(self):
#         print("嗖嗖嗖～")


p01 = Person("老张")
c01 = Car()
a01 = Airplane()
p01.go_to(a01)
