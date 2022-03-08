"""
    字典推导式
"""

# 1 2 3 ... 9 --> 数字:数字的平方
# dict_result = {}
# for item in range(1,10):
#     dict_result[item] = item ** 2
# print(dict_result)

dict_result = {item: item ** 2 for item in range(1, 10)}
dict_result = {item: item ** 2 for item in range(1, 10) if item  % 2 == 0}
print(dict_result)