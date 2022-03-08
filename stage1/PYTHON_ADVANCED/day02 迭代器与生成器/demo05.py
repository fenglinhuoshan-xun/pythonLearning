"""
    yield --> 生成器
"""

"""
    # 生成器：可迭代对象（可以参与for） + 迭代器（产生数据）
    class Generator:
        def __iter__(self):
            return self
            
        def __next__(self):
            ...
"""


def my_range(stop):
    number = 0
    while number < stop:
        yield number
        number += 1


for item in my_range(5):
    print(item)  # 0 1 2 3 4

# 1. 获取迭代器对象
# 延迟操作/惰性操作，即你调我我不干活，等会再做
my = my_range(5)  # 程序不会执行my_range函数，因为yield之前的代码在__next__中。返回的是一个generator对象
iterator = my.__iter__()  # 返回的是一个generator对象，并且和my指向的是同一个对象，即所存储的内存地址相同，因为生成器对象可以点__inter__，所有生成器类中有__iter__方法
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()  # 因为生成器对象可以点__next__方法，所以生成器类中有__next__方法
        print(item)
    # 3. 如果没有元素，则捕获异常，停止循环
    except StopIteration:
        break
