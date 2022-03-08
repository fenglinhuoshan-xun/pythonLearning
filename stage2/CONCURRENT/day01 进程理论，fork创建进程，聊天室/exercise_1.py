"""
有两个函数，一个要执行3秒，一个要执行2秒，编写程序，如何在小于5秒的时间里完成两个函数的执行
"""
import os
from time import sleep


def fun1():
    sleep(2)
    print("fun1 over")


def fun2():
    sleep(3)
    print("fun2 over")

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    fun1()
else:
    fun2()


