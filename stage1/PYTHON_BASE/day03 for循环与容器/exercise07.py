"""
1. 在控制台中获取一个字符串，打印每个字符的编码值
"""
str_input = input("请输入一个字符串:")
for item in str_input:
    number = ord(item)
    print(number)


