"""
进程对象属性
"""
import multiprocessing as mp
from multiprocessing import Process
from time import sleep


def fun():
    print("进程对象属性测试")
    print(mp.current_process().name)
    sleep(3)
    print("进程结束")


p = Process(target=fun, name="Tedu")  # 也可以通过传参的方式来给进程命名。进程名称可以起到对进程的一个基本说明的作用

# 子进程随父进程结束
# p.daemon = True

p.start()
print("PID:", p.pid)  # 如果写在start之前，则为None，因为进程是在start之后才创建起来
print("Name:", p.name)  # 进程名称我们可以通过p.name属性来直接给它赋值
print("is alive：", p.is_alive())
