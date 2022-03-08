"""
    在终端中获取一个四位数，计算每位相加和
    输入：1234
    输出：10
"""
number = int(input("请输入一个四位数："))
# 个位
# number % 10
result = number % 10
# 十位
# number // 10 % 10
result += number // 10 % 10
# 百位
result += number // 100 % 10
# 千位
result += number // 1000
print(result)

qianwei = number // 1000
baiwei = number % 1000 // 100
shiwei = number % 1000 % 100 // 10
gewei = number % 10
all = qianwei + baiwei + shiwei + gewei
print(all)
