"""
UDP服务端
"""
from socket import *

# 创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
sockfd.bind(('0.0.0.0',8888))

# 循环收发消息
while True:
    try:
        data,addr = sockfd.recvfrom(5)
    except KeyboardInterrupt:
        break
    print("Connect from %s:%s" % (addr,data.decode()))
    sockfd.sendto(b'ok',addr)

# 关闭套接字
sockfd.close()