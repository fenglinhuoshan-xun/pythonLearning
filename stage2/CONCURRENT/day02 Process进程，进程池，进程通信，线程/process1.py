"""
process 进程
"""

import multiprocessing as mp
from time import sleep

a = 1


# 进程执行函数
def fun():
    print("开始一个进程")
    sleep(3)
    global a
    print("a = ", a)
    a = 10000  # 在子进程当中修改，只影响子进程，不影响父进程，父子进程空间独立，互不影响
    print(a)
    print("进程结束")


# 创建进程对象
p = mp.Process(target=fun)

p.start()  # 启动进程

sleep(2)  # 看父子进程是否同时执行
print("父进程执行的内容")

p.join()  # 回收进程
print("===============")
print(a)

"""
pid = os.fork()
if pid == 0:
    fun()
    os._exit(0)
else:
    os.wait()
"""
