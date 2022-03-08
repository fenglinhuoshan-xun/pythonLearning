"""
    一个小球从100m的高度落下，每次弹回原高度的一半
    请计算：
    总共经过多少次，最终落地（最小谈起高度0.01m）
    总共经过多少米
"""

height = 100
count = 0
distance = height
while height /2  > 0.01:
    count += 1
    height /= 2  # 弹回原高度的一半
    distance += height * 2 # 累加起落距离
    print("第" + str(count) + "次弹起的高度是" + str(height))
print("总共经过" + str(count) + "次")
print("总共经过" + str(distance) + "米")


# chushi = 100
# count = 0
# juli = 100
# while True:
#     if chushi / 2 >= 0.01:
#         count += 1
#         chushi = chushi / 2
#         juli += chushi * 2
#         print(f"第{count}次弹起的高度是{chushi}")
#     else:
#         break
# print(f"总共经过{count}次，最终落地")
# print(f"总共经过{juli}米")
