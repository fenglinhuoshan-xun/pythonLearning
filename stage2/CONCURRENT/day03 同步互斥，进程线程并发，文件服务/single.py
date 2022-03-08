from test import *
import time

tm = time.time()

for i in range(10):
    # count(1, 1)  # Single cpu: 7.450254440307617 计算密集型程序
    io()  # Single io: 4.202531814575195 IO密集型程序

print("Single cpu:", time.time() - tm)
