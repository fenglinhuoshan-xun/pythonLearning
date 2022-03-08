import time

# 算法1: 三层for循环，执行时间 273.94秒
# start_time = time.time()
#
# for n1 in range(0, 1001):
#     for n2 in range(0, 1001):
#         for n3 in range(0, 1001):
#             if n1 + n2 + n3 == 1000 and n1 ** 2 + n2 ** 2 == n3 ** 2:
#                 print(n1, n2, n3)
#
# end_time = time.time()
# print('执行时间:%.2f' % (end_time - start_time))

# 算法2：两层for循环，执行时间：2.06秒
start_time = time.time()

for n1 in range(0, 1001):
    for n2 in range(0, 1001):
        n3 = 1000 - n1 - n2
        if n1 ** 2 + n2 ** 2 == n3 ** 2:
            print(n1, n2, n3)

end_time = time.time()
print("执行时间：%.2f" % (end_time - start_time))
