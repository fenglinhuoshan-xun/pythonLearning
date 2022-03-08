"""
创建有参数的进程
"""
from multiprocessing import Process
from time import sleep


# 含有参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working...")


# p = Process(target=worker, args=(2, 'Tom'))
# p = Process(target=worker, kwargs={'name': 'Levi', 'sec': 2})
p = Process(target=worker, args=(2,), kwargs={'name': 'Levi'})

p.start()
p.join()
