"""
编写一个服务端程序，同时监控多个客户端发送过来的错误信息，将其写入到一个日志文件中。同时监控服务端的本地输入内容，也写入到
日志中。日志内容包含信息和时间，每条占一行
"""
from select import select
from socket import *
import sys
from time import ctime

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 日志文件
f = open('log.txt', 'a')

s.setblocking(False)

rlist = [s, sys.stdin]
wlist = []
xlist = []

while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is s:
            c, addr = r.accept()
            c.setblocking(False)
            rlist.append(c)
        elif r is sys.stdin:
            f.write("%s %s" % (ctime(), r.readline()))
            f.flush()  # 刷新文件缓存
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            f.write("%s %s\n" % (ctime(), data.decode()))
            f.flush()
