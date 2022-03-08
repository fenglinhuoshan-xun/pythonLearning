"""
    定义函数，计算多个整数每位相加和
    输入：12345
    输出：15
"""


def each_unit_sum(number):
    """
        计算整数的每位相加和
    :param number: int类型，需要操作的数据
    :return: int类型，相加的结果
    """
    sum_value = 0
    for item in str(number):
        # "1" --> 1
        sum_value += int(item)
    return sum_value


re = each_unit_sum(12345)
print(re)
