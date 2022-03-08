"""
基于select的socket复用
"""

from select import select
from socket import *

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

# 创建套接字 作为关注IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

s.setblocking(False)  # 每一个IO任务处理的时间不能太久

rlist = [s]  # 初始关注监听套接字，每次客户端连接的时候是s就绪了
wlist = []
xlist = []

while True:
    # 循环监控IO的发生
    rs, ws, xs = select(rlist, wlist, xlist)

    for r in rs:  # 针对不同的就绪IO，进行不同的操作
        if r is s:
            # 处理客户端连接
            c, addr = r.accept()  # 每次客户端发消息的时候，是c就绪了
            print("Connect from:", addr)
            c.setblocking(False)
            rlist.append(c)
        else:
            data = r.recv(1024).decode()
            if not data:  # 客户端退出
                rlist.remove(r)
                continue
            print(data)
            # r.send(b'OK')
            wlist.append(r)

    for w in ws:
        w.send(b'OK')
        wlist.remove(w)  # 一定要记得使用完IO后，要移除这个就绪IO
