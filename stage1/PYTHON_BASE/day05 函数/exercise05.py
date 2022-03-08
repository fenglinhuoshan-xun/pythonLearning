"""
    方阵转置
"""
# def square_matrix_tranpose(matrix):
#     for c in range(len(matrix) - 1):
#         for r in range(c + 1, len(matrix)):
#             matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
#     return  matrix
#
# list_target = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
# ]
#
# print(square_matrix_tranpose(list_target))

def square_matrix_tranpose(matrix):
    for c in range(len(matrix) - 1):
        for r in range(c + 1, len(matrix)):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    # 因为传入的是一个列表，是可变的对象，函数内部修改了可变对象，所以不用返回值return，也可以。
    # 只要函数内部使用[]，就修改了列表
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

square_matrix_tranpose(list01)
print(list01)