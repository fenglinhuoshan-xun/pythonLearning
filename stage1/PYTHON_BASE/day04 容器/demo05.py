"""
    字典 dict
"""
# 1. 创建
dict01 = {}
dict02 = dict()  # 可以放其他可迭代对象

dict01 = {101: "a", 102: "b", 103: "c"}
dict02 = dict([(101, "a"), (102, "b")])
print(dict02)  # python3.6之后版本，字典打印出来是有顺序的，不过只是一个表象，深层次的还是无序的

# 2. 添加
dict01[104] = "d"  # 104 是一个键，不是索引
print(dict01)

# 3. 修改
dict01[104] = "e"
print(dict01)

# 4. 查找
# key
print(dict01[102])
# 在字典中找东西，一定要先判断一下有没有这个键
if 106 in dict01:
    print(dict01[106]) # 如果字典中没有这个键，则会报错

# 循环
for key in dict01:
    print(key)

for value in dict01.values():
    print(value)
for item in dict01.items():
    print(item)

for k,v in dict01.items():
    print(k)
    print(v)
