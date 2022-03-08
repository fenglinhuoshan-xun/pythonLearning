"""
    函数 -- 应用
"""


# 函数：封装一个特定功能，表示一个行为。在函数的定义中，一个最重要，只做一件事，即一个变化点
#      小而精
# 要是这样写，这份工作就没有了
# 将两个数值相加功能
# def add():
#     numbert_one = float(input("请输入第一个数据："))
#     numbert_two = float(input("请输入第一个数据："))
#     result = numbert_one + numbert_two
#     print("结果是：" + str(result))
#
#
# add()

# 只做和逻辑处理这部分事情，和逻辑处理相关的是你要做的事情，其他无关的通通作为参数和返回值
def add(number_one, number_two):
    return number_one + number_two


numbert_one = float(input("请输入第一个数据："))
numbert_two = float(input("请输入第一个数据："))

result = add(numbert_one,numbert_two)
print("结果是：" + str(result))
