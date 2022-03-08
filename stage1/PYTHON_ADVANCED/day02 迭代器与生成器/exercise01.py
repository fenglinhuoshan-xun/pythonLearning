"""
    创建敌人类，限制攻击力在1 -- 100之间
"""
"""
    异常处理
        主动抛出异常
"""


class AtkRangeError(Exception):
    def __init__(self, name="", error_id=0, error_code=""):
        self.name = name
        self.error_id = error_id
        self.error_code = error_code


class Enemy:
    def __init__(self, age=0):
        self.atk = age

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 1 <= value <= 100:
            self.__atk = value
        else:
            # 如果有多个错误信息（错误名称，错误编号，错误代码...），这时候就应该以面向对象的思想来封装数据了
            # raise Exception("我不要")  # 抛异常
            raise AtkRangeError("攻击力超过范围错误", 1324, "if 1 <= value <= 100")


try:
    mieba = Enemy(400)
except AtkRangeError as e:  # 接收异常
    print(e.name)  # 错误信息可以通过属性点出来
    print(e.error_id)  # 错误信息可以通过属性点出来
    print(e.error_code)  # 错误信息可以通过属性点出来
