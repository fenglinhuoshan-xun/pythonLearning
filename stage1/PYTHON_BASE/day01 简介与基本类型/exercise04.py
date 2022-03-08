"""
练习2：在终端中分别录入3个数据（分钟数，小时数，天数）
      输出总描述
"""

day = float(input("请输入天数："))
hour = float(input("请输入小时数："))
minute = float(input("请输入分钟数："))
result = 24 * 60 * 60 * day + 60 * 60 * hour + 60 * minute
print("总秒数是：" + str(result))
