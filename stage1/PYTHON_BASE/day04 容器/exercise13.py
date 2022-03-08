"""
    自定义排序算法，对列表进行升序排列
    思路：
        依次取出元素，与后面进行比较
        发现更小的，则交换
    输入：[2,8,6,1]
    输出：[1,2,6,8]
"""
list01 = [2, 8, 6, 1]
for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)

# 推导过程
# # list01[0] --> list01[1] list01[2] list01[3]
# for c in range(1, 4):
#     # list01[0] list01[c]
#     pass
#
# # list01[1] --> list01[2] list01[3]
# for c in range(2, 4):
#     # list01[1] list01[c]
#     pass
#
# # list01[2] --> list01[3]
# for c in range(3, 4):
#     # list01[2] list01[c]
#     pass
