"""
ftp 文件服务器 客户端
"""
from socket import *
import sys
import time

# 服务器地址
ADDR = ('127.0.0.1', 8888)


# 具体的请求功能
class FTPClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L')  # 发送请求
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            # 一次性接收所有文件名称 --> "file1\nfile2\n..."
            data = self.sockfd.recv(1024 * 1024)  # 假设1024 * 1024是够用的
            print(data.decode())
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")

    def do_get(self, filename):
        # 发送请求
        self.sockfd.send(("G " + filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            f = open(filename, 'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                f.write(data)
            f.close()
        else:
            print(data)

    def do_put(self, filename):
        try:
            f = open(filename, 'rb')
        except Exception:
            print("该文件不存在")
            return
        # 获取文件名 ../../xxx
        filename = filename.split('/')[-1]
        # 发送请求
        self.sockfd.send(('P ' + filename).encode())
        # 接收反馈
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)


# 搭建网络客户端
def main():
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return

    ftp = FTPClient(s)
    # 循环发送请求
    while True:
        print("\n=========Command==========")
        print("**********   list   **********")
        print("********** get file **********")
        print("********** put file **********")
        print("**********   quit   **********")
        print("===============================")

        cmd = input(">>")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_put(filename)
        else:
            print("请输入正确命令")


if __name__ == '__main__':
    main()
