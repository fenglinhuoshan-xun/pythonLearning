"""
dict 服务端
"""

from socket import *
from multiprocessing import Process
import signal, sys
from dict_db import Database
from time import sleep

# 全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)

# 生成数据库对象
db = Database()


# 处理注册
def do_register(connfd, name, passwd):
    if db.register(name, passwd):
        connfd.send(b"OK")
    else:
        connfd.send(b"FAIL")


def do_login(c, name, passwd):
    if db.login(name, passwd):
        c.send(b'OK')
    else:
        c.send(b'Fail')


# 查询单词
def do_query(c, name, word):
    db.insert_history(name, word)  # 插入历史记录

    # 找到则返回解释，没找到则返回None
    mean = db.query(word)
    if not mean:
        c.send("没有找到该单词".encode())
    else:
        msg = "%s : %s" % (word, mean)
        c.send(msg.encode())


# 历史记录
def do_hist(c, name):
    r = db.history(name)
    if not r:
        c.send(b'Fail')
        return
    c.send(b'OK')

    for i in r:
        # i --> (name,word,time)
        msg = "%s %-16s %s" % i
        sleep(0.1)
        c.send(msg.encode())
    sleep(0.1)  # 防止沾包
    c.send(b'##')


# 处理客户端请求
def handle(connfd):
    db.create_cur()  # 每个子进程单独生成一个游标
    while True:
        # 循环等待客户端发送请求
        data = connfd.recv(1024).decode()
        tmp = data.split(' ')
        # print(connfd.getpeername(), ':', data)
        if not tmp or tmp[0] == 'E':
            return
        elif tmp[0] == 'R':
            do_register(connfd, tmp[1], tmp[2])
        elif tmp[0] == 'L':
            do_login(connfd, tmp[1], tmp[2])
        elif tmp[0] == 'Q':
            do_query(connfd, tmp[1], tmp[2])
        elif tmp[0] == 'H':
            do_hist(connfd, tmp[1])
    db.cur.close()
    connfd.close()


# 程序启动函数
def main():
    # 创建监听套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    print("Listen the port 8000 ....")

    while True:
        # 循环等待客户端连接
        try:
            c, addr = s.accept()
            print("Connect from:", addr)
        except KeyboardInterrupt:  # 按ctrl + c或者红点时，会报这种异常
            s.close()
            db.close()
            sys.exit()  # 人为的希望服务端退出
        except Exception as e:
            print(e)
            continue
        # 创建子进程，处理连接的客户端请求
        p = Process(target=handle, args=(c,))
        p.daemon = True  # 父进程结束则所有服务终止
        p.start()


if __name__ == '__main__':
    main()
