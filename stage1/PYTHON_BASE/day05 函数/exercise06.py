"""
    定义函数计数器，统计函数被调用的次数
"""
count = 0
def fun01():
    global count
    count += 1

fun01()
fun01()
fun01()
print("执行次数是：%d" % count)
