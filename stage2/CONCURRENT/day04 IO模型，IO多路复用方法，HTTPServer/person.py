class Person:
    def __init__(self):
        # self.英俊 = False
        # self.高大 = False
        # self.幽默 = False
        # self.温柔 = False
        # self.善良 = False
        self.属性 = 0
        self.英俊 = 1
        self.高大 = 2
        self.幽默 = 4
        self.温柔 = 8
        self.善良 = 16  # 都是2的次幂，如果都有这些属性，则可表示为11111


小明 = Person()

# 原来的方法
# 小明.高大 = True
# 小明.幽默 = True

小明.属性 = 14

# 给小明设置高大的属性
小明.属性 = 小明.属性 | 小明.高大

# 确定小明是否有高大的属性，True表示有，False表示没有
# if 小明.属性 & 小明.高大:
