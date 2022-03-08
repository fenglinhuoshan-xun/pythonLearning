"""
    bool运算
"""
# 1. 比较运算符
# 参与的数据：主要就是数值
# 比较之后的结果是：bool类型
number01 = 5
number02 = 8
print(number01 > number02)  # 5 > 8
print(number01 < number02)  # 5 < 8
print(number01 == number02)  # 5 = 8
# print(5 > "10") # 不能用整数与字符串进行大小的比较
print(5 == "5") # False 类型不一样

# 2. 逻辑运算符
# 参与的数据：主要就是bool类型的数据，即可以判断命题之间的关系
# 比较之后的结果是：bool类型
# 与 and 一假俱假 假：代表不满足条件 --> 都得满足条件，结论才能满足条件
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# 或 or 一真俱真 --> 一个满足就行 表达或者的关系
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# 非 取反
print(not True)


