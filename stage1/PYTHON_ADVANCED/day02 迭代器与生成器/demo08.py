"""
    函数式编程 -- 思想
"""
list01 = [4, 45, 56, 65, 67, 7]


# 需求1：定义函数，在列表中查找所有大于50的数字
def find01():
    for item in list01:
        if item > 50:
            yield item


# 需求2：定义函数，在列表中查找所有小于10的数字
def find02():
    for item in list01:
        if item < 10:
            yield item


# 函数式编程
# "封装" -- 分
# 分隔变化点，每个变化点做成单独的函数
def condition01(item):
    return item > 50


def condition02(item):
    return item < 10


# 通用代码
# 变量、参数本身就有抽象的特点 "继承" 隔离变化
# 不变的也做成一个通用型函数
def find(func):
    for item in list01:
        # if item > 50:
        # if condition02(item):
        if func(item):
            yield item


# "多态" -- 做
for item in find(condition01):
    print(item)

for item in find(condition02):
    print(item)
