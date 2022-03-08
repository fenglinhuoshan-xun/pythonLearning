"""
    在终端中录入一个成绩，判断等级
    输入：成绩
    输出：优秀、良好、及格、不及格、成绩有误
"""
score = float(input("请输入成绩："))

# if score >= 90 and score <= 100:
#     print("优秀")
#     ...
#
# if 90 <= score <= 100:
#     print("优秀")
#     ...
if score > 100 or score < 0:
    print("成绩有误")
elif score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
