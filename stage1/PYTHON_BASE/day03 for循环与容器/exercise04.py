"""
    随机产生两个数字(1-10)
    在控制台中获取两个数字想加的结果
    如果用户输入正确得10分，否则扣5分
    总共3道题，最后输出得分
    例如："请输入8+3=?"  11  得10分
         "请输入8+3=?"  8  得10分
         "请输入8+3=?"  8  得10分
"""
import random

score = 0
for i in range(3): # 0 1 2 只是为了循环三次
    random_number01 = random.randint(1, 10)
    random_number02 = random.randint(1, 10)
    input_number = int(input("请输入" + str(random_number01) + \
                             "+" + str(random_number02) + "=?"))
    if input_number == random_number01 + random_number02:
        score += 10
    else:
        score -= 5
print("总分是" + str(score))


# count = 0
# for i in range(3):
#     number01 = random.randint(1, 10)
#     number02 = random.randint(1, 10)
#     result = input("请输入%d + %d = ?" % (number01, number02))
#     if result == str(number01 + number02):
#         print("加%d分" % 10)
#         count += 10
#
#     else:
#         print("扣%d分" % 5)
#         count -= 5
# print("您最终得分%d分" % count)

