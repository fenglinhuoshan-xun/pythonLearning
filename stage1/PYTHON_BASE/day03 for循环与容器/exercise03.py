"""
累加10-50之间个位不是2,5,9的整数
"""
count = 0
for unit in range(10, 51):
    unit = unit % 10
    if unit == 2 or unit == 5 or unit == 9:
        continue
    count += unit
print(count)