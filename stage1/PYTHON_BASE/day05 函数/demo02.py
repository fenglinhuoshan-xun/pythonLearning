"""
    函数 -- 返回值
"""


def fun01():
    print("fun01执行喽")
    return 100  # 返回100


number = fun01()  # number这个变量绑定了100的地址
print(number)


def fun02():
    print("fun01执行喽")
    return  # return关键字后面如果没有数据，相当于返回None
    # 如果函数没有返回值，即没有return关键字，在别的语言中就报错了，但在python中，也相当于返回None


re = fun02()
print(re)

# 即使有返回值，调用者仍然可以不使用变量来接收，全靠调用者个人需求

# fun01()


