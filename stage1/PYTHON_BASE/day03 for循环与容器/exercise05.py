"""
在终端中录入一个整数，判断是否为素数
素数：只能被1和自身整除的正数
思路：排除法，使用2到当前数字之间的正数判断，如果存在被整除，则不是素数
判断9：
    能否被2 -- 8之间的数字整除，其中3可以，所以不是素数
判断8：
    能否被2 -- 7之间的数字整除，其中2可以，所以不是素数
判断7：
    能否被2-- 6之间的数字整除，其中没有，所以是素数
2  3  5  7  11  13  15 ...
"""

number = int(input("请输入一个整数："))

for i in range(2, number):
    if number % i == 0:
        print("不是素数")
else:
    print("是素数")


# number = int(input("请输入一个整数："))
# count = 0
# for i in range(2, number):
#     if number % i == 0:
#         count += 1
# if count > 0:
#     print("%d不是素数" % number)
# else:
#     print("%d是素数" % number)
