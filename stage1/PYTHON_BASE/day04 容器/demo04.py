"""
    元祖
"""
# 1. 创建
tuple01 = ()
tuple01 = tuple()

tuple01 = (12,33,4)
list01 = ["a","b","c"]
tuple02 = tuple(list01)
print(tuple02)
list03 = list(tuple02)

tuple02 = (1,) # 元祖中如果只有一个元素，后面需要加,
tuple02 = 1,2,3 # 小括号可以省略
print(tuple02)

# 2. 查询
tuple03 = ("a","b","c")
a,b,c = tuple03 # 对于列表，这样子操作也可以
# 索引
print(tuple03[-1])

# 切片
print(tuple03[:2])

# 循环
for item in tuple02:
    print(item)




