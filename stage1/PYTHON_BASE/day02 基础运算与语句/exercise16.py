"""
游戏运行产生一个1 -- 100之间的随机数
让玩家重复猜测，直到猜对了为止
输出：大了、小了、猜对了，总共猜了多少次
提示：
    # 随机数工具(在开头写一次)
    import random

    # 产生一个随机数
    random_number = random.randint(1,100)
"""

import random

random_number = random.randint(1, 100)
count = 0
while True:
    count += 1
    guess = int(input("请输入你猜测的数字："))
    if guess > random_number:
        print("你猜大了")
    elif guess < random_number:
        print("你猜小了")
    else:
        print("猜对了，总共猜了" + str(count) + "次")
        break


# while True:
#     guess = int(input("请输入你猜测的数字："))
#     if guess > random_number:
#         print("你猜大了")
#         count += 1
#     elif guess < random_number:
#         print("你猜小了")
#         count += 1
#     else:
#         print("猜对了")
#         break
# print("总共猜了%d次" % count)
