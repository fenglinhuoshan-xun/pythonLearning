"""
    函数
"""


def attack():  # 程序是自上而下执行的，将代码加载到内存当中
    """
        攻击函数
    """
    print("侧踹")
    print("直拳")
    print("摆拳")
    print("勾拳")
    print("肘击")


attack()
# ...
attack()


# 有参数的函数
# 形式参数
def attack_repeat(count):  # 在python中，函数名称可以一样，不报错，但建议还是遵守规范
    """
        重复攻击
    :param count: int类型，重复的次数
    """
    for i in range(count):
        print("侧踹")
        print("直拳")
        print("摆拳")
        print("勾拳")
        print("肘击")


# 实际参数
attack_repeat(3)

# attack()


"""
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
# ........
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
# ........
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
"""
