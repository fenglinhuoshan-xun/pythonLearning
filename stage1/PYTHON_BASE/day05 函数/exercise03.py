"""
    定义函数，根据成绩计算等级
    输入：96
    输出：优秀
"""


# def get_score_level(score):
#     if score < 0 or score > 100:
#         return "成绩输入有误"
#     elif 90 <= score:
#         return "优秀"
#     elif 80 <= score:
#         return "良好"
#     elif 60 <= score:
#         return "及格"
#     else:
#         return "不及格"

def get_score_level(score):
    if score < 0 or score > 100:  # 因为有return，return代表有结果，函数一旦有了结果，就会退出函数，# 所以可以将elif改为if
        return "成绩输入有误"  # return可以简化程序，简化逻辑
    if 90 <= score:
        return "优秀"
    if 80 <= score:
        return "良好"
    if 60 <= score:
        return "及格"
    else:
        return "不及格"


print(get_score_level(96))
