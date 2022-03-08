"""
    创建老婆类，老婆列表
    定义下列函数：
        1)获取所有老婆姓名
        2)获取颜值大于80的所有老婆对象
        3)获取年龄最大的老婆对象
        4)根据颜值对老婆列表进行升序排列
"""


class Wife:
    def __init__(self, name="", face_score=0, age=0):
        self.name = name
        self.face_score = face_score
        self.age = age

    def print_self(self):
        print(self.name, self.face_score, self.age)


list_wife = [
    Wife("阿珂", 100, 23),
    Wife("苏荃", 92, 32),
    Wife("双儿", 90, 25),
    Wife("小郡主", 76, 22),
    Wife("方怡", 75, 27),
    Wife("建宁", 86, 25),
    Wife("曾柔", 67, 24),
]


# 1)获取所有老婆姓名
def find01():
    result = []
    for item in list_wife:
        result.append(item.name)
    return result


print(find01())


# 2)获取颜值大于80的所有老婆对象
def find02():
    result = []
    for item in list_wife:
        if item.face_score > 80:
            result.append(item)
    return result


for item in find02():
    item.print_self()


# 3)获取年龄最大的老婆对象
def get_max():
    max_value = list_wife[0]
    for i in range(1, len(list_wife)):
        if max_value.age < list_wife[i].age:
            max_value = list_wife[i]
    return max_value


re = get_max()
re.print_self()


# 4)根据颜值对老婆列表进行升序排列
# 传入可变，修改可变，可以不需要返回值，原数据就变了
def order_by():
    for r in range(len(list_wife) - 1):
        for c in range(r + 1, len(list_wife)):
            if list_wife[r].face_score > list_wife[c].face_score:
                list_wife[r], list_wife[c] = list_wife[c], list_wife[r]


order_by()
print("-----------")
for item in list_wife:
    item.print_self()
