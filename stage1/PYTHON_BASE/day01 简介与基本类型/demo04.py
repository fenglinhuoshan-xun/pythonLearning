"""
    核心数据类型
        变量没有类型，关联的对象才有类型
"""

name = "lzmly"

# 1. None 空
skill = None
# ...
skill = "乾坤大挪移"

# 解除与对象的绑定关系
name = None

# 2. 整形（整数）
# 十进制：0 1 2 3 ... 9 逢10进1，此位变0
# 二进制：0 1 10 11 100 101 逢2进1，此位变0
number01 = -1
number01 = 1
number01 = 0

number02 = 0b10
print(number02)

# 八进制：0 1 2 3 ... 7 10
number03 = 0o10
print(number03)

# 十六进制：0 1 2 ... 9 a(10) ... f(15) 10 11
number04 = 0x11
print(number04)

# 3. 浮点型（小数）浮点型在内存的存储形式就是科学计数法
number05 = 1.0
number06 = 5e3
print(number06)

number07 = 0.000005
print(number07)

# 4. 字符串（文字）
name = "lzmly"
str_number = "1000"
# 数学运算
result = 1000 + 1
# 文字拼接
result = "1000" + "1"
print(result)

# 5. 数据类型转换
# input函数的返回值永远都是字符串类型
# str_number = input("请输入一个数字：")

# str --> int
# print(type(str_number))
# re = int(str_number)

# str --> float
# re = float(str_number)
# print(type(re))
# print(re)

# 注意：int()转换时，数据必须像整数
# 注意：float()转换时，数据必须像小数

# 其他类型 --> str
re = str(100.6)
print(type(re))
