"""
    生成器表达式
"""
# 列表推导式
list01 = [34, 43, 54, 65, 67, 7]
list02 = [item for item in list01 if item > 10]
for item in list02:
    print(item)

# 生成器表达式
generator02 = (item for item in list01 if item > 10)
for item in generator02:
    print(item)

# 开发时，经常这样写
for item in (item for item in list01 if item > 10):
    print(item)

# 在开发时什么时候用生成器表达式，什么时候用生成器函数？
# 生成器表达式用于比较简单的逻辑，就算是针对比较简单的逻辑，生成器表达式和生成器函数也是不一样的，生成器表达式是我做我用，生成器函数是我做，别人用
