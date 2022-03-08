"""
    运算符重载（在其他语言中叫做运算符重载，在python中叫做运算符重写）
        作用：让自定义的类生成的对象，即自定义对象使用python运算符
"""


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x的分量是%d,y的分量是%d" % (self.x, self.y)

    # +：返回新对象
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    # +=：返回自己，即原对象
    def __iadd__(self, other):
        self.x += other.x  # 要返回自己，在内部就要完成对自己的修改
        self.y += other.y
        return self  # 返回自己

    # <
    def __lt__(self, other):
        return self.x + self.y < other.x + other.y

    # ==
    def __eq2__(self, other):
        return self.x == other.x and self.y == other.y


pos = Vector2(1, 2)
dir = Vector2(0, 1)
# 算数运算符
# print(pos + dir)  # 本质就相当于pos.__add__(dir)，调用上面的__add__方法，传入dir，pos传给了self，dir传给了otherl

# pos.x += dir.x
# pos.v += dir.y
# 复合运算符
pos += dir  # 我们会发现，只是重写了__add__，就已经实现了功能，但是我们实际上的+=应该是复合运算符__iadd__，那这时候__add__已经把它的事干了，那为什么还要有__iadd__？一定是有区别的
print(pos)

"""
# +：创建了新对象
list01 = [1]
print(id(list01))
list01 = list01 + [2]
print(id(list01))

# +=：累加（在原有对象基础上增加，能在原有对象基础上就在原有对象基础上，如果是个元祖，才创建新对象）
list02 = [1]
print(id(list02))
list02 += [2]
print(id(list02))
"""

# 在编程中其实就没有什么加减乘除，背后都是一些方法，为了迎合数学，让我们用的方便，所有才搞出了加减乘除这些符号

# 练习：参照上述代码，重写2个算数运算符
# pos *= dir
# print(pos)

list01 = [
    Vector2(1, 2),
    Vector2(7, 8),
    Vector2(5, 6),
    Vector2(3, 4),
]

# sorted升序排列：内部在循环调用每个元素的__lt__方法
for item in sorted(list01):
    print(item)

# in：in的内部也在循环调用每个元素的__eq__方法
print(Vector2(1, 2) in list01)

# remove方法：如果没有这个元素，就会报错，我们如果没有重写__eq__方法，就会报错
list01.remove(Vector2(1, 2))
print(len(list01))
# count：表示元素出现的次数，我们如果没有重写__eq__方法，就会报错
list01.count(Vector2(1, 2))
