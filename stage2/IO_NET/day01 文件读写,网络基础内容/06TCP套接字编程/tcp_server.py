"""
TCP服务端流程
"""

import socket

#创建tcp套接字
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('127.0.0.1',8888))

#设置监听
sockfd.listen(3)

#等待处理客户端连接,如果一个客户端退出，服务端等待连接其他客户端
while True:
    print("Waiting for connect...")
    try:
        connfd,addr=sockfd.accept()
        print("Connect from",addr)
    except KeyboardInterrupt: #让程序退出的优雅一点
        print("Server exit")
        break

    #收发内容
    while True:
        data=connfd.recv(1024)
        if data=="%".encode():
            break
        print("Receive:",data.decode())
        n=connfd.send(b"Thanks")
        print("Send %d bytes"% n)
    connfd.close()

#关闭套接字

sockfd.close()