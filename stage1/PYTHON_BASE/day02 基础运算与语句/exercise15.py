"""
一张纸的厚度是0.01毫米，请计算对折多少次，超过珠穆朗玛峰8844.43米
答案：30次
"""

thickness = 1e-5
count = 0
while thickness < 8844.43:
    # 对折一次
    thickness *= 2
    count += 1
    print("第" + str(count) + "次对折的厚度是：" + str(thickness))
print(count)




# thickness = 0.01
# count = 0
# while thickness <= 8844.43 * 10 ** 3:
#     count += 1
#     thickness = 0.01 * 2 ** count
#     print("第" + str(count) + "次对折的厚度是：" + str(thickness))
# print(count)