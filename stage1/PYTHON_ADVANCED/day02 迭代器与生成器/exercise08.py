"""
    1. 使用生成器表达式在list01中找出所有字符串
    2. 使用生成器表达式找出所有大于10的整数
"""
list01 = ["悟空", 57, "八戒", True, "三藏", 5.8, 10, 90]

for element in (item for item in list01 if type(item) == str):
    print(element)

for element in (item for item in list01 if type(item) == int and item > 10):
    print(element)
