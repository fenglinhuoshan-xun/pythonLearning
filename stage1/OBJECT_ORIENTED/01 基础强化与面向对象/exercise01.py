"""
    创建狗类
    数据成员包含但不限定于：品种、爱你、年龄、性别
    方法成员包含但不限定于：吃
    创建两个对象并调用方法
"""


class Dog():
    """
        狗
    """

    def __init__(self, breed="", name="", age=0, sex=""):
        self.breed = breed
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print(self.name, "吃")


d01 = Dog("拉布拉多", "米咻", 4, "母")
d02 = Dog("拉布拉多", "黑米", 3, "公")

d01.eat()
d02.eat()

# 练习1：根据下列代码画出内存图
d03 = d01
d01.age = 5
print(d03.age)  # ? 5
d04 = d02
d02 = Dog("哈士奇", "二哈", 2, "公")  # ? 黑米
print(d04.name)


# 练习2：根据下列代码画出内存图
def fun01(p01):
    p01.name = "哈哈哈"


fun01(d02)
print(d02.name)  # ? 哈哈哈

list01 = [
    d01,
    d02,
    Dog("沙皮", "皮皮", 3, "公"),
    Dog("金毛", "毛毛", 3, "母"),
]


# 练习3：定义函数，在狗列表中查找所有拉布拉多
def find01():
    list_result = []
    for item in list01:
        if item.breed == "拉布拉多":
            list_result.append(item)
    return list_result


re = find01()
for item in re:
    print("----")
    print(item.name)
