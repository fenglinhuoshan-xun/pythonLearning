"""
chat room # 项目的大体含义
env: python3.6 # 所用的环境
socket udp & fork # 运用的基本技术以及作者的姓名和邮箱
"""

from socket import *
import os, sys

# 服务器地址，一般情况下，我们在编程过程当中，会把一些重要的有特殊意义的变量定义为全局变量
# 也有的时候，我们发现某个变量在大多数模块、函数或者类中都有应用的话，我们也可以把这种变量定义为全局变量
ADDR = ('0.0.0.0', 8888)

# 存储用户信息 {name: address}
user = {}


# 登录操作
def do_login(s, name, addr):
    if name in user or '管理员' in name:
        s.sendto("该用户存在".encode(), addr)
        return
    s.sendto(b'ok', addr)
    # 通知其他人
    msg = "\n欢迎‘%s’进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr


# 聊天处理
def do_chat(s, name, text):
    msg = "\n%s：%s" % (name, text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])


# 退出处理
def do_quit(s, name):
    msg = "\n%s退出聊天室" % name
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b'EXIT', user[i])  # 让其本人退出


# 不断的接收客户端请求
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        tmp = data.decode().split(' ', 2)  # tmp --> ['L',..]，最多切割前两项
        # 请求分发，判断请求类型，交给后续的功能去处理
        if tmp[0] == 'L':  # 客户端想登录
            do_login(s, tmp[1], addr)
        elif tmp[0] == 'C':
            do_chat(s, tmp[1], tmp[2])
        elif tmp[0] == 'Q':
            do_quit(s, tmp[1])


# 网络搭建
def main():
    # udp服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid == 0:
        while True:
            msg = input("管理员消息：")
            msg = "C 管理员 " + msg
            s.sendto(msg.encode(), ADDR)  # 把消息从子进程发送给自己，即父进程
    else:
        do_request(s)


if __name__ == '__main__':
    main()
