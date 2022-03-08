"""
    创建图形管理器：
        1. 记录所有图形
        2. 计算总面积
    图形:
        1. 矩形
        2. 圆形
        ...
    要求：
        增加新图形，管理器代码不变

    画出设计图
    写出哪里体现了四大原则
        开闭原则：增加新图形，管理器代码不变
        单一职责：Rectanlge 负责举行面积的算法，Circle 负责图形面积的算法
        GraphicManager 负责统一管理图形
        依赖倒置：图形管理起没有调用圆形、矩形算法、而是调用图形类
        组合服用：图形管理器与具体的各种图形是组合关系
"""


class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def calculate_total_area(self):
        total_area = 0
        for item in self.__graphics:
            total_area += item.get_area()
        return total_area


class Graphic:
    def get_area(self):
        pass


# -----------------------
class Rectanlge(Graphic):
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


class Circle(Graphic):
    def __init__(self, radius=0):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2


manager = GraphicManager()
manager.add_graphic(Rectanlge(2, 6))
manager.add_graphic(Circle(5))
print(manager.calculate_total_area())
