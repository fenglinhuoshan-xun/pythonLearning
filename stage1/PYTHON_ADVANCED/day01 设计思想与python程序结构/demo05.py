"""
    时间处理
"""
import time

# 1. 获取当前时间戳：从1970年1月1日到现在经过的秒数
print(time.time())  # 记录用时间戳 1633614099.8401837    给计算机看的

# 2. 获取当前时间元组（年、月、日、时、分、秒、星期几、这一年的第几天、夏令时），星期几是索引，比真实的星期几少1
time_tuple = time.localtime()
print(time_tuple)  # 显示用时间元组   给人看的

# 3. 时间戳 --> 时间元组
print(time.localtime(1633614099.8401837))

# 4. 时间元祖 --> 时间戳
print(time.mktime(time_tuple))

# 5. 时间元组 --> 字符串 # 格式是固定的
print(time.strftime("%y/%m/%d %H:%M:%S", time_tuple))  # y：2位
print(time.strftime("%Y/%m/%d %H:%M:%S", time_tuple))  # Y：4位

# 6. 字符串 --> 时间元组
time.strptime("21/10/07 22:21:38", "%y/%m/%d %H:%M:%S")
