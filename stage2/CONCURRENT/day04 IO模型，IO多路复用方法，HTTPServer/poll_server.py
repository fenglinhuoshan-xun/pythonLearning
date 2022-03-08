"""
基于poll方法的socket服务
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

# 生成poll对象
p = poll()
p.register(s, POLLIN)

# 建立查找字典，时刻与关注的IO保持一致
fdmap = {s.fileno(): s}

# 循环监控IO发生
while True:
    events = p.poll()  # [(3, 1),(),...]
    for fd, events in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from:", addr)
            c.setblocking(False)
            p.register(c, POLLIN | POLLNVAL)
            fdmap[c.fileno()] = c
        elif events & POLLIN:  # 看POLLIN是否就绪
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                del fdmap[fd]
                continue
            print(data)
            fdmap[fd].send(b'OK')
