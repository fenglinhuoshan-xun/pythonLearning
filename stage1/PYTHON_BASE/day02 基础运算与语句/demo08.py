"""
    猜数字2.0版本
        如果猜错次数超过5次，则结束游戏，并提示"失败了"
"""

import random

random_number = random.randint(1, 100)
print(random_number)
count = 0

while count < 5:
    count += 1
    if count > 5:
        print("失败了")
        break
    guess = int(input("请输入你猜测的数字："))
    if guess > random_number:
        print("你猜大了")
    elif guess < random_number:
        print("你猜小了")
    else:
        print("猜对了，总共猜了" + str(count) + "次")
        break
else:
    # 当循环不满足条件时退出，猜执行一下代码
    print("失败了")

# while True:
#     count += 1
#     if count > 5:
#         print("失败了")
#         break
#     guess = int(input("请输入你猜测的数字："))
#     if guess > random_number:
#         print("你猜大了")
#     elif guess < random_number:
#         print("你猜小了")
#     else:
#         print("猜对了，总共猜了" + str(count) + "次")
#         break