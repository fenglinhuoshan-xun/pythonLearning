"""
自定义进程类
"""
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, value):
        self.value = value  # 添加自己的属性
        super().__init__()

    def fun1(self):
        print("工作步骤1")

    def fun2(self):
        print("工作步骤2")

    def run(self):
        self.fun1()
        self.fun2()


if __name__ == '__main__':
    p = MyProcess(2)
    p.start()  # 调用start()，自动执行run()方法
    p.join()  # 回收子进程
