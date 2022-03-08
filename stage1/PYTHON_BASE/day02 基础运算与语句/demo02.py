"""
    逻辑运算符的短路逻辑
"""
# 启发：逻辑运算时，尽量将复杂的（耗时的）判断放在后面
# False and ?
re = 1 > 1 and input("请输入：") == "a"
print(re)

# True or ?
re = 2 > 1 or input("请输入") == "a"
print(re)

