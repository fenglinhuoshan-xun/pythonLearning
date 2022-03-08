"""
基于thread的多线程并发
"""
from socket import *
import os
from threading import Thread

# 全局变量
ADDR = ('0.0.0.0', 8888)


# 客户端处理函数
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()


# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

# 循环等待客户端连接
print("Listen the port 8888 ....")
while True:
    try:
        c, addr = s.accept()
        print("Connect from:", addr)
    except KeyboardInterrupt:  # 按ctrl + c或者红点时，会报这种异常
        s.close()
        os._exit()  # 人为的希望服务端退出
    except Exception as e:
        print(e)
        continue
    # 创建线程，处理连接的客户端请求
    t = Thread(target=handle, args=(c,))
    t.setDaemon(True)
    t.start()
