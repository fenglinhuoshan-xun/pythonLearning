"""
    练习：对象计数器
        使用类变量记录
        使用类方法打印
"""


class Wife:
    count = 0

    @classmethod
    def print_count(self):
        print("总共娶了",self.count,"个")

    def __init__(self):
        Wife.count += 1


w01 = Wife()
w02 = Wife()
w03 = Wife()
w04 = Wife()
w05 = Wife()

Wife.print_count()