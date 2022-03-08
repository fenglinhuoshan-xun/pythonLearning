"""
    使用for循环绘制下列图形：
    *****
    #####
    *****
    #####
"""
for r in range(4):  # 0 1 2 3
    for c in range(5):
        if r % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()
