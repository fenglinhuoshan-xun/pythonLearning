"""
递归
"""


def f(n):
    if n == 0:
        return
    print(n)
    f(n - 1)


f(3)


# 输出结果：3 2 1

def f(n):
    if n == 0:
        return
    f(n - 1)
    print(n)


f(3)


# 输出结果：1 2 3
# 总结经典2句话：
# 1. 调用递归之前的语句，从外到内执行（递推过程中执行）
# 2. 调用递归之后的语句，从内到外执行（回归过程中执行）
# 3. 递归一定会有递推和回归两个过程

# 练习；计算1 + 2 + 3 + ... + n的和
def sumn(n):
    if n == 1:
        return 1
    return n + sumn(n - 1)


print(sumn(5))

# print(sum(1000))  # maximum recursion depth exceeded in comparison
print(sumn(998))
