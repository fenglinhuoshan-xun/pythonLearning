"""
    装饰器
"""


def func01():
    print("func01执行喽")
    return "ok"


def func02(a):
    print(a, "func02执行喽")


# 装饰器的核心逻辑：就是在调用的时候，改变它的调用
# 我们想在不改变原函数（指func01()，func02()）的调用以及内部代码（指func01，func02）的情况下，增加这个新功能
def print_func_name(func):
    # wrapper直译过来就是包。我们需要一个包，想把新旧功能都包在一起
    def wrapper(*args, **kwargs):  # 合
        # 新功能
        print(func.__name__)
        # 旧功能
        # 如果想拿到旧功能的返回值，则内部函数的返回值应为旧功能的返回值
        return func(*args, **kwargs)  # 拆

    return wrapper


# 我们期待func01 = 新功能 + 旧功能
# func01 = print_func_name + func01
func01 = print_func_name(func01)  # func01指向的是wrapper函数的内存地址

print(func01())

func02 = print_func_name(func02)

func02(100)
