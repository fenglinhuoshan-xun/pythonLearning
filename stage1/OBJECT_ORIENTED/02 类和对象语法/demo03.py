"""
    静态方法引入
    也就是从需求上讲，我们总是会获取某一个位置，某一个方向上指定数量的元素，我们应该以面向对象的思想，将这些
    所谓的位置啊方向啊用一个对象来表达，然后这个东西经常需要用一些函数，这些函数是面向过程的，不符合面向对象的开发
    所以我们要把它做成类中的静态方法
"""
list01 = [
    ["00", "01", "02", "03", "04"],
    ["10", "11", "12", "13", "14"],
    ["20", "21", "22", "23", "24"],
    ["30", "31", "32", "33", "34"],
]


# 表达元素位置
class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def get_right():
    return Vector2(0, 1)


pos = Vector2(2, 1)
right = get_right()
pos.x += right.x
pos.y += right.y
print(pos.x)
print(pos.y)


# 需求：30位置上向右获取三个元素
def get_elements(list_target, vect_pos, vect_dir, count):
    list_result = []
    for __ in range(count):
        vect_pos.x += vect_dir.x
        vect_pos.y += vect_dir.y
        element = list_target[vect_pos.x][vect_pos.y]
        list_result.append(element)
    return list_result


print(get_elements(list01, Vector2(3, 0), get_right(), 3))
