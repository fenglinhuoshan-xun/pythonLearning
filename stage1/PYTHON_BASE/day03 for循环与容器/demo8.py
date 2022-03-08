"""
    列表内存分配
"""
list01 = [10, 20]
list02 = list01
list01[0] = 100
print(list02[0])  # ? 100

list01 = [10, 20]
list02 = list01
list01 = 100
print(list02[0])  # ? 10

list01 = [10, 20]
list02 = list01[:]
list01[0] = 100
print(list02[0])  # ? 10

list01 = [10, [20, 30]]
list02 = list01
list01[1][0] = 100
print(list02[1][0])  # ? 100

import copy

list01 = [10, [20, 30]]
lsit02 = list01[:]  # 浅拷贝
list03 = list01  # 赋值
list04 = copy.deepcopy(list01) # 深拷贝
# 深拷贝
# 优点：互不影响
# 缺点：往往占用内存过多

