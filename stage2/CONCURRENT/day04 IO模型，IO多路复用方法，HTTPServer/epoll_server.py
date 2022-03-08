"""
基于epoll方法的socket服务
"""

from select import *
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

# 生成epoll对象
ep = epoll()
ep.register(s, EPOLLIN)

# 建立查找字典，时刻与关注的IO保持一致
fdmap = {s.fileno(): s}

# 循环监控IO发生
while True:
    events = ep.poll()  # [(3, 1),(),...]
    print("你有一个IO需要处理：", events)
    for fd, events in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from:", addr)
            c.setblocking(False)
            ep.register(c, EPOLLIN | EPOLLET)  # 边缘触发
            fdmap[c.fileno()] = c
        # elif events & EPOLLIN:  # 看POLLIN是否就绪
        #     data = fdmap[fd].recv(1024).decode()
        #     if not data:
        #         ep.unregister(fd)
        #         del fdmap[fd]
        #         continue
        #     print(data)
        #     fdmap[fd].send(b'OK')
