"""
    在终端中录入月份，然后打印天数
    输入：2 输出：28天
    输入：1 3 5 7 8 10 12 输出：31天
    输入：4 6 9 11 输出：30天
"""
month = int(input("请输入月份："))
if month < 1 or month > 12:
    print("月份输入有误")
elif month == 2:
    print("28天")
elif month == 4 or month == 6 or month == 9  or month == 11:
    print("30天")
else:
    print("31天")

