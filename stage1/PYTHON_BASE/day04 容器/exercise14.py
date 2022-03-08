"""
    打印二维列表第四行第三列元素
    从左到右打印二维列表第二行所有元素
    从上到下打印二维列表第一列所有元素
    将二维列表按照表格状输出到终端
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

print(list01[3][2])

for item in list01[1]:
    print(item, end=" ")

print()

# list01[0][0]
# list01[1][0]
# list01[2][0]
# list01[3][0]
for r in range(4):
    print(list01[r][0])

# for item in list01:
#     print(item[0])

for line in list01:
    for item in line:
        print(item, end="\t")
    print()

# for r in range(4):
#     for c in range(4):
#         print(c + 1 + r * 4, end="\t")
#     print()
