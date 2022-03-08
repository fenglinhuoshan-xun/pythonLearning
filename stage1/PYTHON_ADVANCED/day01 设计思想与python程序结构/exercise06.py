"""
    定义函数，获取成绩（0 -- 100）
"""


def get_score():
    while True:
        try:
            score = int(input("请输入成绩："))
        except:
            print("输入的不是整数")
            continue
        if 0 <= score <= 100:
            return score
        else:
            print("成绩输入超过范围")


score = get_score()
print(score)
