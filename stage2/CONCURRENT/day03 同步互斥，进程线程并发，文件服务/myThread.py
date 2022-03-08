"""
自定义线程类
"""
from threading import Thread
from time import sleep, ctime


# 自定义的线程类
class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs={}):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args, **self.kwargs)


def player(song, sec):
    for i in range(3):
        print("Playing %s : %s" % (song, ctime()))


t = MyThread(target=player, args=('葫芦娃', 2))
t.start()
t.join()
