"""
    定义父类：
        车(数据：品牌，价格)
    定义子类：
        电动车(数据：充电速度，电池容量)
"""


class Car:
    def __init__(self, brand="", price=0):
        self.brand = brand
        self.price = price


# 重写：子类具有与父类相同名称的方法，这个时候就会把父类的方法给覆盖，这个时候我们再去调用子类的构造函数的时候，就好像父类的不存在一样
class Electrocar(Car):
    def __init__(self, brand="", price=0, charging_speed=0, battery_capacity=0):
        super().__init__(brand, price)
        self.charging_speed = charging_speed
        self.battery_capacity = battery_capacity


e01 = Electrocar("宝马", 300000, 60, 10000000)
