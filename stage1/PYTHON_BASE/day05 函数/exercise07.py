"""
    定义函数：根据小时、分钟、秒计算总秒数
    要求：
        根据小时、分钟、秒
        根据小时、分钟
        根据分钟、秒
        根据分钟
"""
def get_total_second(hour = 0,minute = 0,second = 0):
    return hour * 3600 + minute * 60 + second


print(get_total_second(1, 2, 3))
print(get_total_second(1, 2))
print(get_total_second(minute=2, second=3))
print(get_total_second(minute=2))

