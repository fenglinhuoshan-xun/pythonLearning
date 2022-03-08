"""
    函数式编程 -- 语法
"""


def func01():
    print("func01执行")


# 注意不能写小括号，写小括号相当于把返回值给到了变量，这个函数返回值为None
# 如果把函数名给到变量，相当于变量也指向函数的内存地址
a = func01
a()


def func02():
    print("func02执行")


# 通过代码
def func03(func):
    print("func03执行")
    func()


func03(func02)
func03(func01)
