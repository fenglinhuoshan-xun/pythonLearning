"""
在控制台中获取一个整数作为边长，打印矩形
输入：4
输出：
    ****
    *  *
    *  *
    ****
"""
number = int(input("请输入整数："))
print("*" * number)
for i in range(number-2):
    print("*" + " " * (number-2) + "*")
print("*" * number)

