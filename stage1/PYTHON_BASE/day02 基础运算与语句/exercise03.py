"""
    在终端中获取总秒数，计算几小时零几分零几秒
    输入：10000
    输出；2小时零46分钟零40秒
"""

total_second = int(input("请输入总秒数："))
hour = total_second // 60 // 60
minute = total_second // 60 % 60
second = total_second % 60
print(str(hour) + "小时零" + str(minute) + "分钟零" + str(second) + "秒")

# total_second = int(input("请输入总秒数："))
# hour = total_second // (60 * 60)
# minute = total_second % (60 * 60) // 60
# second = total_second % 60
# print(f"{hour}小时零{minute}分钟零{second}秒")
