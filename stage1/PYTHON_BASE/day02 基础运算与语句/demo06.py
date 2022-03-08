"""
    while 循环
"""
# 死循环
while True:
    number = int(input("请输入一个整数："))
    state = "奇数" if number % 2 else "偶数"
    print(state)
    if input("请输入exit退出：") == "exit":
        break  # 退出循环
