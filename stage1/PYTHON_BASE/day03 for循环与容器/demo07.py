"""
    列表
"""
# 1. 创建列表
list01 = []
list02 = list()

list01 = [90, "唐僧", True]
# 根据其他可迭代对象
list02 = list("我是齐天大圣")
print(list02)

# 2. 添加
# -- 追加
list01.append("悟空")
# -- 插入
list01.insert(2, "八戒")
print(list01)

# 3. 获取
# 索引：单个
print(list01[-1])

# 切片：多个
# 通过切片，会创建新列表
print(list01[:3])

# 循环：所有
for item in list01:
    print(item)

# 倒序
# 因为切片会产生新列表，会浪费内存，所以不建议下面的方式
# for item in list01[::-1]:
#     print(item)
for i in range(len(list01)-1,-1,-1):
    print(list01[i])


# 4. 修改
# 索引
# 将右侧的数据地址赋值给左侧定位的元素
list01[-1] = "end"
print(list01)
# 切片
# 遍历右侧的可迭代对象，将每个元素赋值给左侧定位的元素
# list01[:2] = [1,2]
print(list01)
# list01[:2] = [1,2,3,4,5,6,7,8,9,10]
# list01[:3] = []
list01[1:1] = [1,2,3,4]
print(list01)

# 循环
for item in range(len(list01)):
    list01[item] = None
print(list01)

# 5. 删除
print(list02)
# 根据元素移除
list02.remove("我")
print(list02)

# 根据索引、切片移除
del list02[-1]
del list02[:2]
print(list02)
