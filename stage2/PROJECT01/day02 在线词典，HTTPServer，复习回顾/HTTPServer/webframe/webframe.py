"""
模拟实现后端应用
"""

from socket import *
import json
from settings import *
from threading import Thread
from urls import *


# 应用类：用于实现基础的数据处理
# 处理请求
class Application(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

    def get_html(self, info):
        if info == '/':
            filename = STATIC + '/index.html'
        else:
            filename = STATIC + info
        try:
            fd = open(filename)
        except Exception as e:
            with open(STATIC + '/404') as f:
                return {'status': '404', 'data': f.read()}
        else:
            return {'status': '200', 'data': fd.read()}

    # 处理非网页情况
    def get_data(self, info):
        for url, func in urls:
            if url == info:
                return {'status': '200', 'data': func()}
        return {'status': '404', 'data': 'Sorry ...'}

    # 执行线程功能
    def run(self):
        # 接收请求 {'method':'GET','info':'xxxx'}
        request = self.connfd.recv(1024).decode()
        request = json.loads(request)  # 转换为python的字典
        if request['method'] == 'GET':
            # 根据情况调用函数，返回值即得到的数据 --> {}
            if request['info'] == '/' or request['info'][-5:] == '.html':  # 请求的是网页
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])
        elif request['method'] == 'POST':
            pass
        # 数据发送给httpserver
        response = json.dumps(response)
        self.connfd.send(response.encode())
        self.connfd.close()


# 搭建网络模型
def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
    s.bind((frame_ip, frame_port))

    s.listen(3)
    print("Listen the port 8800")
    while True:
        c, addr = s.accept()
        print("Connect from:", addr)

        # 创建线程
        app = Application(c)
        app.setDaemon(True)
        app.start()


if __name__ == '__main__':
    main()
