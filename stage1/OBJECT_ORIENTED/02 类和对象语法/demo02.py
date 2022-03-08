"""
    类成员
        类变量：
"""


class ICBC:
    """
        工商银行
    """
    # 类变量：表示大家的数据，定义在类中，方法外
    # 类变量是类级别的变量，所有对象都能共享
    total_money = 1000000

    # 类方法：建议用类方法来操作类变量
    @classmethod
    def print_total_money(cls):
        # 在类方法中访问类变量，也可以通过类名去点
        # print("总行的钱：",ICBC.total_money)
        # 建议用这种写法，因为有时候类名比较长
        print("总行的钱：", cls.total_money)

    def __init__(self, name="", money=0):
        self.name = name
        self.money = money
        # 类变量是类级别的变量，想要在实例方法中访问，要用类名去点
        # 总行的钱减少
        ICBC.total_money -= money


i01 = ICBC("陶然亭支行", 100000)
# print(ICBC.total_money)
ICBC.print_total_money()
i02 = ICBC("天坛支行", 100000)
# print(ICBC.total_money)
ICBC.print_total_money()
