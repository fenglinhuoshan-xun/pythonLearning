"""
    异常处理
        主动抛出异常
"""


class AgeRangeError(Exception):
    def __init__(self, name="", error_id=0, error_code=""):
        self.name = name
        self.error_id = error_id
        self.error_code = error_code


class Wife:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            # 如果有多个错误信息（错误名称，错误编号，错误代码...），这时候就应该以面向对象的思想来封装数据了
            # raise Exception("我不要")  # 抛异常
            raise AgeRangeError("年龄超过范围错误", 1324, "if 20 <= value <= 30")


try:
    shuanger = Wife(40)
except AgeRangeError as e:  # 接收异常
    print(e.name)  # 错误信息可以通过属性点出来，接收多个信息，放在一个元组里
    print(e.error_id)  # 错误信息可以通过属性点出来
    print(e.error_code)  # 错误信息可以通过属性点出来
