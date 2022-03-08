"""
    迭代器 --> yield
"""


class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        # 现象：调用__iter__方法，代码不执行，调用__next__方法，代码执行
        # 你看见的代码，不是这样子的
        # 代码生成大致流程:
        # 1. 以yeild为界限，将__iter__方法中的代码分割为几部分，最后一部分为抛异常。如代码被分为4部分，最后一部分为抛异常
        # 1. 将yield以前的代码，定义在__next__方法中
        # 2. 将yield后面的数据，作为__next__方法的返回值
        # print("准备")
        # yield self.__skills[0]  # yield：产生
        # print("准备")
        # yield self.__skills[1]
        # print("准备")
        # yield self.__skills[2]
        for item in self.__skills:
            print("准备")
            yield item


manager = SkillManager()
manager.add_skill("九阳神功")
manager.add_skill("乾坤大挪移")
manager.add_skill("太极")

for item in manager:
    print(item)

