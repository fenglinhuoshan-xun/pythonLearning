"""
多线程及线程传参
"""
from threading import Thread
from time import sleep


def music(sec, name):
    sleep(2)
    print("播放%s" % name)


l = ['黄河大合唱', '国际歌', '中国心']
jobs = []
for i in l:
    t = Thread(target=music, args=(2, i))
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()
