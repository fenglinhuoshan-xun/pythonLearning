"""
模拟迅雷下载文件
使用多个线程从不同地方拷贝一个文件，每个线程负责拷贝文件的一部分
"""

from threading import Thread, Lock
import os

lock = Lock()
urls = ['/home/xiaoshoubingliang/桌面/',
        '/home/xiaoshoubingliang/文档/',
        '/home/xiaoshoubingliang/视频/',
        '/home/xiaoshoubingliang/下载/',
        '/home/xiaoshoubingliang/音乐/',
        '/home/xiaoshoubingliang/图片/',
        '/home/xiaoshoubingliang/']

filename = input("要下载的文件：")
explorer = []
for i in urls:
    if os.path.exists(i + filename):
        explorer.append(i + filename)
path_num = len(explorer)

if path_num == 0:
    os._exit(0)  # 退出进程

file_size = os.path.getsize(explorer[0])
block_size = file_size // path_num

fd = open(filename, 'wb')


def load(path, num):
    f = open(path, 'rb')
    seek_num = block_size * (num)
    f.seek(seek_num)
    data = f.read(block_size)  # 模拟下载过程
    with lock:
        fd.seek(seek_num)
        fd.write(data)


num = 0
jobs = []
for path in explorer:
    t = Thread(target=load, args=(path, num))
    jobs.append(t)
    t.start()
    num += 1

for i in jobs:
    i.join()
