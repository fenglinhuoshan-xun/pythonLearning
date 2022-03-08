"""
    装饰器
"""


def print_func_name(func):
    def wrapper(*args, **kwargs):  # 合
        # 新功能
        print(func.__name__)
        # 旧功能
        return func(*args, **kwargs)  # 拆

    return wrapper


@print_func_name  # 这句话原理等同于func01 = print_func_name(func01)，即调用上面的代码，传入参数，再给到func01
def func01():
    print("func01执行喽")
    return "ok"


@print_func_name  # func02 = print_func_name(func02)
def func02(a):
    print(a, "func02执行喽")


# 我们期待func01 = 新功能 + 旧功能
# func01 = print_func_name + func01

print(func01())

func02(100)
