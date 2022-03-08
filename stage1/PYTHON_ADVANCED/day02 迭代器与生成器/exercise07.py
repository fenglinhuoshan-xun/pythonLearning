"""
    参照下列代码，自定义生成器my_zip
"""


# 自定义生成器
# 取相同位置的元素，通过索引去取
def my_zip(iterable01, iterable02):  # *args
    for i in range(len(iterable01)):  # 判定长度
        yield iterable01[i], iterable02[i]


list01 = ["八戒", "悟空", "苏大强"]

list02 = [102, 105]

# for item in my_zip(list01, list02):
#     print(item)

# zip：将多个可迭代对象的元素一一对应，组合成一个元组，元组数量由小的可迭代对象决定
for item in zip(list01, list02, list02, list02):
    print(item)

# range() 也是python内置的一个生成器
