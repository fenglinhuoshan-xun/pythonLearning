"""
    练习1:在老婆列表中,查找颜值大于90的所有老婆
    练习2:在老婆列表中,查找身高小于170的所有老婆
"""

class Wife:
    def __init__(self, name="", face_score=0, age=0, height=0):
        self.name = name
        self.face_score = face_score
        self.age = age
        self.height = height


list_wife = [
    Wife("双儿", 96, 22, 166),
    Wife("阿珂", 100, 23, 173),
    Wife("小郡主", 96, 22, 161),
    Wife("方怡", 86, 27, 166),
    Wife("苏荃", 99, 31, 176),
    Wife("建宁", 93, 24, 163),
    Wife("曾柔", 88, 26, 170),
]



def find01():
    for item in list_wife:
        if item.face_score > 90:
            yield item


def find02():
    for item in list_wife:
        if item.height < 170:
            yield item


def condition01(item):
    return item.face_score > 90


def condition02(item):
    return item.height < 170


def find(func):
    for item in list_wife:
        # if item.face_score > 90:
        # if condition01(item):
        if func(item):
            yield item


for item in find(condition01):
    print(item)

for item in find(condition02):
    print(item)
