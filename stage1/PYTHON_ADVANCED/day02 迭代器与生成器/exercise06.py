"""
    参照下列代码，自定义生成器my_enumerate
"""


# 自定义的生成器
def my_enumerate(iterable):
    index = 0
    for item in iterable:
        yield (index, item)
        index += 1


dict01 = {"悟空": 26, "八戒": 28}
for item in my_enumerate(dict01):
    print(item)

# enumerate：将索引和元素进行拼接，形成一个元组
for item in enumerate(dict01):
    print(item)  # (0, '悟空') (1, '八戒')

for i, b in enumerate(dict01):
    print(i, b)  # 0 悟空 1 八戒
