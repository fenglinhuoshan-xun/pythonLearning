"""
    集合 set
        1. 价值：去重复
        2. 数学运算
"""
# 1. 创建
set01 = set()

set02 = {"唐僧", "悟空", "八戒"}

list01 = ["A", "b", "c", "A"]
set03 = set(list01)
print(set03)  # 无序的，每次运行，哈希运算的结果不同，结果会去重

print(set("abcaacdb"))

# 2. 添加
set01.add("A")
set01.add("A")
print(set01)

# 3. 删除
set02.remove("唐僧")
if "唐三藏" in set02: set02.remove("唐三藏")  # 报错：KeyError: '唐三藏'。可以事先判断一下
print(set02)

# 4. 循环
for item in set02:
    print(item)

# 5. 数学运算
set04 = {1, 2, 3}
set05 = {2, 3, 4}
# -- 交集
print(set04 & set05)  # {2, 3}
# -- 并集
print(set04 | set05)  # {1, 2, 3, 4}
# -- 补集
print(set04 ^ set05)  # {1, 4}
print(set04 - set05)  # {1}
print(set05 - set04)  # {4}
# -- 子集
set06 = {2, 3}
print(set06 < set04)  # True
# -- 超集
print(set04 > set06)  # True