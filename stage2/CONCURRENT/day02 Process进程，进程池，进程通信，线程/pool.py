"""
进程池
"""
from multiprocessing import Pool
from time import sleep
import os


# 进程池事件，要求写在进程池创建之前
def fun(msg):
    sleep(2)
    print(os.getpid(), ":", msg)
    return msg


# 创建进程池对象
pool = Pool(4)

# 添加进程事件
for i in range(10):
    msg = "Tedu%d" % i
    pool.apply_async(func=fun, args=(msg,))  # 你一添加事件，进程就已经执行了，但是如果此时运行，什么都不会打印，因为父进程执行完了，进程池被销毁
    # r = pool.apply_async(func=fun, args=(msg,))
    pool.apply(func=fun, args=(msg,))  # 也可以将事件放在进程池等待队列。顺序执行，就是说你必须执行完一个事件后，再执行另外一个事件，不管进程池中有多少个进程，都要一个一个执行

# 一旦父进程执行完毕，所有的进程池对象都会被销毁
# sleep(3)  # 5191 : Tedu1 5192 : Tedu0

# 关闭进程池
pool.close()

# 回收进程池
pool.join()
# print(r.get())  # Tedu9
