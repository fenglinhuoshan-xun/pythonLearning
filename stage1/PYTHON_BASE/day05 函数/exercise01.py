"""
将下列代码，定义到函数中，打印矩形
    for r in range(3):
        for c in range(5):
            print("*",end=" ")
        print()
"""


def print_rectangle(r_count, c_count, char):  # 写函数，要有服务意识，尽可能的让程序灵活一些
    for r in range(r_count):
        for c in range(c_count):
            print(char, end=" ")
        print()


print_rectangle(5, 3, "*")
