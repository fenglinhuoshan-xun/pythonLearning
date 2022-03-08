"""
多线程示例
"""
import threading
from time import sleep
import os

a = 1


def fun():
    print("开始一个线程", os.getpid())  # 9459
    sleep(3)
    global a
    print('a = ', a)  # 1
    a = 10000
    print("结束")


t = threading.Thread(target=fun)  # 创建线程对象
t.start()  # 启动线程

sleep(2)
print("主线程内容", os.getpid())  # 9459

t.join()  # 回收线程
print('a:', a)  # 10000
