"""
    需求1：
        1. 在老婆列表中查找方怡对象
        2. 在老婆列表中查找颜值大于95的单个老婆对象
        first

    需求2：
        1. 计算老婆列表中姓名大于2个字的老婆数量
        2. 计算老婆列表中年龄小于25的老婆数量
        get_count

    需求3：
        1. 获取老婆列表中所有老婆的姓名
        2. 获取老婆列表中所有老婆的姓名与颜值
        select

    需求4：
        1. 在老婆列表中判断是否存在姓名是苏荃的元素
        2. 在老婆列表中判断是否存在高度大于170的元素
        is_exists

    需求5：
        1. 累加老婆列表中所有人的年龄
        2. 累加老婆列表中所有人的高度
        sum

    需求6：
        1. 在老婆列表中找出颜值最高的老婆对象
        2. 在老婆列表中找出年龄最大的老婆对象
        get_max

    需求7：
        1. 在老婆列表中删除年龄小于25的所有老婆
        2. 在老婆列表中删除身高大于170的所有老婆
        delete_all

    需求8：
        1. 对老婆列表根据年龄进行生序排列
        2. 对老婆列表根据颜值进行生序排列
        order_by

    步骤：
        1. 根据需求，定义函数
        2. 将变化点单独定义为函数
        3. 将通用代码定义为函数，使用参数来隔离变化点
        4. 在IterableHelper类中添加新功能
        5. 在当前模块中进行测试
"""
from common.iterable_tools import IterableHelper


class Wife:
    def __init__(self, name="", face_score=0, age=0, height=0):
        self.name = name
        self.face_score = face_score
        self.age = age
        self.height = height

    def __str__(self):
        return "%s-%d-%d-%d" % (self.name, self.face_score, self.age, self.height)


list_wife = [
    Wife("双儿", 96, 22, 166),
    Wife("阿珂", 100, 23, 173),
    Wife("小郡主", 96, 22, 161),
    Wife("方怡", 86, 27, 166),
    Wife("苏荃", 99, 31, 176),
    Wife("建宁", 93, 24, 163),
    Wife("曾柔", 88, 26, 170),
]

# def condition01(item):
#     return item.face_score > 90


# for item in IterableHelper.find_all(list_wife, condition01):
#     print(item)
for item in IterableHelper.find_all(list_wife, lambda item: item.face_score > 90):
    print(item)

# 练习1：
# 1. 在老婆列表中查找方怡对象，如果考虑返回重名的，可以用yield
# def first01():
#     for item in list_wife:
#         if item.name == "方怡":
#             return item  # 返回单个结果


# 2. 在老婆列表中查找颜值大于95的单个老婆对象
# def first02():
#     for item in list_wife:
#         if item.face_score > 95:
#             return item  # 返回单个结果

# def condition01(item):
#     return item.name == "方怡"


# def condition02(item):
#     return item.face_score > 95


# def first(func):
#     for item in list_wife:
#         # if item.face_score > 95:
#         # if condition02(item):
#         if func(item):
#             return item

# print(IterableHelper.first(list_wife, condition02))
print(IterableHelper.first(list_wife, lambda item: item.face_score > 95))

# 练习2
# 1. 计算老婆列表中姓名大于2个字的老婆数量
# 2. 计算老婆列表中年龄小于25的老婆数量
# def condition01(item):
#     return len(item.name) > 2


# def condition02(item):
#     return item.age < 25


# def get_count(func):
#     count = 0
#     for item in list_wife:
#         if func(item):
#             count += 1
#     return count


# print(IterableHelper.get_count(list_wife, condition01))
print(IterableHelper.get_count(list_wife, lambda item: len(item.name) > 2))

# 练习3：
# 1. 获取老婆列表中所有老婆的姓名
# 2. 获取老婆列表中所有老婆的姓名与颜值

# def handle01(item):
#     return item.name


# def handle02(item):
#     return (item.name, item.face_score)


# def select(func):
# for item in list_wife:
#     yield func(item)

# for item in IterableHelper.select(list_wife, handle02):
#     print(item)

for item in IterableHelper.select(list_wife, lambda item: (item.name, item.face_score)):
    print(item)

# 练习4：
# 1. 在老婆列表中判断是否存在姓名是苏荃的元素
# 2. 在老婆列表中判断是否存在高度大于170的元素
# def is_exists(func):
#     for item in list_wife:
#         if func(item):
#             return True
#     return False

print(IterableHelper.is_exists(list_wife, lambda item: item.name == "苏荃"))
print(IterableHelper.is_exists(list_wife, lambda item: item.height > 170))

# 练习5：
# 1. 累加老婆列表中所有人的年龄
# 2. 累加老婆列表中所有人的高度
# def sum(func):
#     sum_value = 0
#     for item in list_wife:
#         sum_value += func(item)
#     return sum_value


print(IterableHelper.sum(list_wife, lambda item: item.age))
print(IterableHelper.sum(list_wife, lambda item: item.height))

# 练习6：
# 1. 在老婆列表中找出颜值最高的老婆对象
# 2. 在老婆列表中找出年龄最大的老婆对象
# def get_max(func01, func02):
#     max_value = func01(item)
#     for i in range(1, len(list_wife)):
#         if max_value < func02(i):
#             max_value = func02(i)
#         return max_value


# print(IterableHelper.get_max(list_wife, lambda: list_wife[0].face_score, lambda i: list_wife[i].face_score))
# print(IterableHelper.get_max(list_wife, lambda: list_wife[0].age, lambda i: list_wife[i].age))
# print(IterableHelper.get_max(list_wife, lambda element: element.height))

# 练习7：
# 1. 在老婆列表中删除年龄小于25的所有老婆
# 2. 在老婆列表中删除身高大于170的所有老婆

# print(IterableHelper.delete_all(list_wife, lambda e: e.age > 25))

# 练习8：
# 1. 对老婆列表根据年龄进行生序排列
# 2. 对老婆列表根据颜值进行生序排列
IterableHelper.order_by(list_wife, lambda e: e.age)
for item in list_wife:
    print(item)
