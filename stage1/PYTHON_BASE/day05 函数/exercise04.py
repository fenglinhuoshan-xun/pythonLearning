"""
    定义函数，判断列表中是否存在相同元素
    输入：[3,4,6,8,6]
    输出：True
"""


def is_repeating(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True  # return执行完了依旧会退出，因为纵使循环再多，return退出的是函数


list01 = [3, 4, 6, 8, 6]
print(is_repeating(list01))

# list[0] --> list[1]
# list[2]
# list[3]
# lsit[1] --> list[2]
# list[3]
# list[2] --> list[3]
