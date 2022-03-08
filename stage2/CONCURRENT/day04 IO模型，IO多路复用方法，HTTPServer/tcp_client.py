"""
tcp 客户端流程
"""

from socket import *

# 创建tcp套接字
# sockfd = socket(family=AF_INET,type=SOCK_STREAM,proto=0)  # 默认值
sockfd = socket()  # 默认值

# 连接服务端
server_addr = ('127.0.0.1', 8888)
sockfd.connect(server_addr)

# 收发消息
while True:
    msg = input(">>")
    # 如果直接回车，不发消息，我们break退出
    # if not msg:
    #     break
    sockfd.send(msg.encode()) # 转化为字节串，一个普通的tcp套接字
    if msg == '##':
        break
    data = sockfd.recv(1024)
    print("From server:", data.decode()) # 转化为字符串

# 关闭套接字
sockfd.close()
