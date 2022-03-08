"""
    外部嵌套作用域
"""


def func01():
    a = 10

    def func02():
        # 内部函数可以访问外部嵌套变量
        # 外部嵌套变量：指外部嵌套作用域中的变量
        # print(a) # 10
        # a = 20 # 只写这句话是在给func02创建了一个局部变量
        # 内部函数如果想要修改外部嵌套变量，需要使用nonlocal语句声明
        nonlocal a
        a = 20

    func02()
    print(a)


func01()
