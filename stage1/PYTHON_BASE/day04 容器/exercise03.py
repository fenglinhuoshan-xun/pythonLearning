"""
    生成1-10之间的数字，将其平方存入list01中
    将list01中所有奇数存入list02中
    将list01中所有大于5的偶数增加1后存入list03中
"""
list01 = [item ** 2 for item in range(1, 11)]
list02 = [item for item in list01 if item % 2]
list03 = [item + 1 for item in list01 if item % 2 == 0 and item > 5]

