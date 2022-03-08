"""
    内置高阶函数
        高阶函数：指这个函数的参数或者返回值是函数
"""


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

# 1. map：映射
# 在老婆列表中获取所有名称
# 它的返回值，因为它返回的结果是多个的，所以用到了生成器，返回的是生成器对象
# 类似于自定义的select函数
for element in map(lambda item: item.name, list_wife):
    print(element)

# 2. filter：过滤器
# 在老婆列表中获取颜值大于90的所有老婆
# 类似于自定义的find_all函数
for element in filter(lambda item: item.face_score > 90, list_wife):
    print(element)

# 3. max/min
# 在老婆列表中获取颜值最高的老婆
# 类似于自定义的get_max函数
print(max(list_wife, key=lambda item: item.face_score))
print(min(list_wife, key=lambda item: item.face_score))

# 4. sorted：排序，返回的是一个列表。并没有改变原有的列表，而是返回新的列表
# 升序
for item in sorted(list_wife, key=lambda item: item.height):
    print(item)

# 降序
for item in sorted(list_wife, key=lambda item: item.height, reverse=True):
    print(item)
