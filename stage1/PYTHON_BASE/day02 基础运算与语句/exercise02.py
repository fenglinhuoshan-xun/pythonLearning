"""
在终端中录入距离，时间，初速度，计算加速度
匀变速直线运动的位移和时间公式：
    距离=初速度 * 时间 + 加速度 * 时间平方的一半
输入：
    距离：100
    初速度：2
    时间：5
输出：加速度7.2
"""

distance = float(input("请输入距离："))
initial_velocity = float(input("请输入初速度："))
time = float(input("请输入时间："))
accelerated_speed = 2 * (distance - initial_velocity * time) / (time ** 2)
print("加速度：" + str(accelerated_speed))