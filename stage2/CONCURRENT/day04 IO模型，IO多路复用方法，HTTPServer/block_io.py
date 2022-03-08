"""
非阻塞IO
"""
from socket import *
from time import *

s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 套接字变为非阻塞
# s.setblocking(False)

# 设置超时时间
s.settimeout(3)

while True:
    print("Waiting for connect...")
    try:
        c, addr = s.accept()  # BlockingIOError
    except (BlockingIOError, timeout) as e:
        print(e)
        sleep(2)
    else:
        print("Connect from:", addr)
        data = c.recv(1024)  # 如果想让这个recv也变成非阻塞，则可以设置c这个套接字为非阻塞
