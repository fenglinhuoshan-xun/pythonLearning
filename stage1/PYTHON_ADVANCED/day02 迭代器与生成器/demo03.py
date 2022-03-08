"""
    迭代器
    目的：迭代自定义对象，即让自定义的对象可以参与for循环
    自定义对象：自定义的类生成的对象
"""


# 自己写的，名字无所谓
class SkillIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > len(self.__data) - 1:
            raise StopIteration()
        return self.__data[self.__index]


class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        return SkillIterator(self.__skills)  # 返回的对象要有__next__方法


manager = SkillManager()
manager.add_skill("九阳神功")
manager.add_skill("乾坤大挪移")
manager.add_skill("太极")


# for item in manager:
#     print(item)

# 需求
iterator = manager.__iter__()  # 要求manager对象要有__iter__方法
while True:
    try:
        item = iterator.__next__()  # 要求返回的对象要有__next__方法
        print(item)  # 要求一次打印出列表中的数据
    except StopIteration:
        break
