"""
    list 推导式
"""
# 只要是根据另外一个可迭代对象来构造列表的时候，就可以用列表推导式了
list01 = [5,56,67,7,89]
# list02 = []
# for item in list01:
#     list02.append(item + 1)

list02 = [item + 1 for item in list01]

print(list02)

# list03 = []
# for item in list01:
#     if item % 2 == 0:
#         list03.append(item)

list03 = [item for item in list01 if item % 2 == 0]
print(list03)
