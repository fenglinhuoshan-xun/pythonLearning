from multiprocessing import Process
from time import sleep
import os


def fun1():
    sleep(3)
    print(os.getppid(), '--', os.getpid(), "吃饭")


def fun2():
    sleep(2)
    print(os.getppid(), '--', os.getpid(), "睡觉")


def fun3():
    sleep(4)
    print(os.getppid(), '--', os.getpid(), "打豆豆")


jobs = []
for th in [fun1, fun2, fun3]:
    p = Process(target=th)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()
