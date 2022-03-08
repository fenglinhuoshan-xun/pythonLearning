"""
在控制台中录入日期（月日），计算是这一年的第几天
例如；
    3月15日 --> 31 + 28 + 15
    5月20日 --> 31 + 28 + 31 + 30 + 20
"""
month = int(input("请输入月份："))
day = int(input("请输入天数："))
day_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)
# total_day = 0
# for item in day_of_month[:month-1]:
#     total_day += item
total_day = sum(day_of_month[:month-1])
total_day += day
print(total_day)
