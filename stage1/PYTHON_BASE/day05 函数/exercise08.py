"""
    定义函数，多个数值累加，
"""

# def sum(*args):
#     sum_value = 0
#     for item in args:
#         sum_value += item
#     return sum_value
#
#
# print(sum(213, 3, 4, 3, 5, 6, 67))
# print(sum())

def sum(args):
    sum_value = 0
    for item in args:
        sum_value += item
    return sum_value


print(sum([213, 3, 4, 3, 5, 6, 67]))
print(sum([]))
