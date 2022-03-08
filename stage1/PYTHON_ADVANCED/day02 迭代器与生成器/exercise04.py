"""
    for item in Myrange(5):
        print(item) # 0 1 2 3 4
"""


class MyRangeIterator:
    def __init__(self, stop):
        self.__number = -1
        self.__stop_value = stop

    def __next__(self):
        self.__number += 1
        if self.__number >= self.__stop_value:
            raise StopIteration()
        return self.__number


class MyRange:
    def __init__(self, stop):
        self.__stop = stop

    def __iter__(self):
        return MyRangeIterator(self.__stop)


# 担不担心会撑爆内存？
# 不担心，循环一次，计算一次，返回一次，得到一个数字
for item in MyRange(999999999999999999999999999999):
    print(item)  # 0 1 2 3 4

for item in MyRange(5):
    print(item)  # 0 1 2 3 4
