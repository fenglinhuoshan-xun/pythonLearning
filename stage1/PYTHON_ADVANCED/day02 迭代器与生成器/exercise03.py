"""
    迭代员工管理器
"""
"""
    迭代器
    目的：迭代自定义对象，即让自定义的对象可以参与for循环
    自定义对象：自定义的类生成的对象
"""


# 自己写的，名字无所谓
class EmployeeIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > len(self.__data) - 1:
            raise StopIteration()
        return self.__data[self.__index]


class EmployeeManager:
    def __init__(self):
        self.__employees = []

    def add_employee(self, employee):
        self.__employees.append(employee)

    def __iter__(self):
        return EmployeeIterator(self.__employees)  # 返回的对象要有__next__方法


manager = EmployeeManager()
manager.add_employee("八戒")
manager.add_employee("悟空")
manager.add_employee("张无忌")

for item in manager:
    print(item)

# 需求
# iterator = manager.__iter__()  # 要求manager对象要有__iter__方法
# while True:
#     try:
#         item = iterator.__next__()  # 要求返回的对象要有__next__方法
#         print(item)  # 要求一次打印出列表中的数据
#     except StopIteration:
#         break
