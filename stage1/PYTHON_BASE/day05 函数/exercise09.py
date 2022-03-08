"""
    调用下列函数
"""


def fun01(*args, **kwargs):
    print(args)
    print(kwargs)


fun01()
fun01(1, 2, 3, a=1, b=2)


def fun02(a, *args, b, c="", **kwargs):
    print(a)
    print(args)
    print(b)
    print(c)
    print(kwargs)


fun02(1, 2, 3, b=2, c="3", d=4)
fun02(a=1, b=2, )
