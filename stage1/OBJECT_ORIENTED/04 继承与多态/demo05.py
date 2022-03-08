"""
    设计思想 -- 引入
        老张开车去东北
        变化点：飞机、火车、轮船
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle):
        print("走喽")
        if type(vehicle) == Car:
            vehicle.run()
        elif type(vehicle) == Airplane:
            vehicle.fly()


class Car:
    def run(self):
        print("嘟嘟嘟~")


class Airplane:
    def fly(self):
        print("嗖嗖嗖~")


p01 = Person("老张")
c01 = Car()
a01 = Airplane()
p01.go_to(a01)
