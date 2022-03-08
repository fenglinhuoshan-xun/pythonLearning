"""
    2048 核心算法
         降维
"""
list_merge = [2, 0, 0, 2]


# 1. 定义函数，将list_merge中的零元素移动到末尾
# [2,0,0,2] --> [2,2,0,0]
# [4,0,4,0] --> [4,4,0,0]
def zero_to_end():
    """
        零元素移动到末尾
        思路：从后往前依次判断，如果是零元素，则删除后追加零
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 测试
# zero_to_end()
# print(list_merge)


# 2. 定义函数，将list_merge中的元素进行合并（相邻且相同）
# [2,0,0,2] --> [2,2,0,0,] --> [4,0,0,0]
# [4,0,4,0] --> [4,4,0,0,] --> [8,0,0,0]
# [2,2,2,2] --> [4,4,0,0]
def merge():
    """
        合并
        思路：
            将零元素后移
            判断如果相邻且相同则合并
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# merge()
# print(list_merge)

map = [
    [2, 0, 0, 2],
    [2, 4, 4, 2],
    [0, 4, 2, 0],
    [2, 0, 2, 0],
]


# 3. 定义函数，将二维列表map中的元素向左移动
def move_left():
    """
        向左移动
        思路：将每行（一维列表）赋值给全局变量list_merge
             再通过merge函数操作数据
    """
    global list_merge
    for line in map:
        list_merge = line
        merge()


# move_left()
# print(map)


# 4. 定义函数，将二维列表map中的元素向右移动
def move_right():
    """
        向右移动
        思路：将每行（反向切片）赋值给全局变量list_merge
             再通过merge函数操作数据
             再对list_merge（反向切片）
    """
    global list_merge
    for line in map:
        # 因为切片，所以创建了新列表
        list_merge = line[::-1]
        merge()  # 操作的是新列表
        line[::-1] = list_merge


# move_right()
# print(map)


def square_matrix_tranpose(matrix):
    for c in range(len(matrix) - 1):
        for r in range(c + 1, len(matrix)):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


# 5. 定义函数，将二维列表map中的元素向上移动
def move_up():
    """
        思想：方针转置
             调用向左移动
             方阵转置
    """
    square_matrix_tranpose(map)
    move_left()
    square_matrix_tranpose(map)


# 6. 定义函数，将二维列表map中的元素向下移动
def move_down():
    """
        思想：方针转置
             调用向右移动
             方阵转置
    """
    square_matrix_tranpose(map)
    move_right()
    square_matrix_tranpose(map)

move_down()
print(map)
