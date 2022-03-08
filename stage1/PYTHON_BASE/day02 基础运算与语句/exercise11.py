"""
1. 在终端中获取一个整数，如果是偶数，为变量state赋值"偶数"，否则赋值"奇数"
2. 在终端中获取一个年份，如果是闰年，为变量day赋值29,否则赋值28
"""
# 1.
number = int(input("请输入一个整数："))
state = "奇数" if number % 2 else "偶数"
print(state)

# 2.
year = int(input("请输入年份："))
# 代码可读性强
# day = 29 if year % 4 == 0 and year % 100 !=0 or year % 400 == 0 else 28
# 不建议
day = 29 if not year % 4 and year % 100 or not year % 400  else 28
print(day)