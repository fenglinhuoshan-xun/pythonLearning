"""
ftp 文件服务器服务端
env：python3.6
多线程 tcp并发
"""

from socket import *
from threading import *
import os, sys
import time

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
FTP = '/home/xiaoshoubingliang/FTP/'  # 文件库位置


# 自定义线程类
# 客户端处理类 查看服务器 上传 下载
class FTPSever(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

    def do_list(self):
        # 获取文件列表
        file_list = os.listdir(FTP)
        if not file_list:
            self.connfd.send("文件库为空")
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)

            # 发送文件
            # files = ""
            # for file in file_list:
            #     files += file + '\n'
            files = '\n'.join(file_list)
            self.connfd.send(files.encode())

    def do_get(self, filename):
        try:
            f = open(FTP + filename, 'rb')
        except Exception as e:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)

        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        f.close()

    def do_put(self, filename):
        if os.path.exists(FTP + filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b'OK')
        # 接收文件
        f = open(FTP + filename, 'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    def run(self):
        # 接收客户端请求
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == 'Q':
                return
            elif data == 'L':
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)


# 启动函数
# 搭建网络模型
def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)
    print("listen the port 8888")
    # 循环等待客户端连接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from:", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务端退出")
        except Exception as e:
            print(e)
            continue

        t = FTPSever(c)
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    main()
