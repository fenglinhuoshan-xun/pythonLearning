"""
消息队列
"""
from multiprocessing import Process, Queue
from time import sleep

# 创建消息队列
# 注意创建消息队列的位置：我们需要在父进程中创建消息队列，所有的子进程都使用父进程的这个队列对象。用的是同一个队列对象，所有自然而然就能通信了
q = Queue(3)


def bar():
    for i in range(5):
        sleep(2)
        q.put("hello")


def foo():
    while True:
        try:
            print(q.get(timeout=3))
        except:
            return


p1 = Process(target=bar)
p2 = Process(target=foo)
p1.start()
p2.start()
p1.join()
p2.join()
