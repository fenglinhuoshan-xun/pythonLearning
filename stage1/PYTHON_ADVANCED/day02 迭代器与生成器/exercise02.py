"""
    练习1：使用迭代思想，获取元组中所有元素
    练习2：使用迭代思想，获取字典中所有k，v
"""
tuple01 = (1, 2, 3, 4)
dict01 = {"唐僧": 27, "悟空": 29, "八戒": 30}

iterator = tuple01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

iterator = dict01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item, dict01[item])
    except StopIteration:
        break
