from socket import *
from select import select


# 具体功能 --> 帮助使用者很简单的搭建http服务
class HTTPServer:
    def __init__(self, host='0.0.0.0', port=80, dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host, port)
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.creat_socket()
        self.bind()

    # 创建套接字
    def creat_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.setblocking(False)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)

    # 启动服务，做所有的跟接收客户端请求相应的工作
    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d" % self.port)
        self.rlist.append(self.sockfd)
        while True:
            # 循环监控IO的发生
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:  # 针对不同的就绪IO，进行不同的操作
                if r is self.sockfd:
                    # 处理客户端连接
                    c, addr = r.accept()  # 每次客户端发消息的时候，是c就绪了
                    print("Connect from:", addr)
                    c.setblocking(False)
                    self.rlist.append(c)
                else:
                    # 处理客户端请求
                    self.handle(r)

    # 具体处理客户端请求
    def handle(self, connfd):
        # 获取请求，将请求内容提取出来
        data = connfd.recv(4096)  # 接收请求
        # 防止浏览器异常退出
        if not data:
            self.rlist.remove(connfd)
            connfd.close()  # 不再关注这个连接对象
            return
        request_line = data.decode().split('\n')[0]  # 请求行
        info = request_line.split(' ')[1]  # 请求内容
        print("请求内容：", info)

        # 对请求内容进行分类处理
        # 网页：/    xxx.htlml    其他：
        # 要具体思考服务端收到请求该做什么事 --　组织数据，回发给客户端
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd, info)
        else:
            self.get_data(connfd, info)

    # 处理网页
    def get_html(self, connfd, info):
        # 请求主页
        if info == '/':
            filename = self.dir + '/index.html'
        # 请求其他的
        else:
            filename = self.dir + info
        try:
            fd = open(filename)
        except:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry...</h1>"

        else:
            response = "HTTP/1.1 200 ok\r\n"  # 响应行
            response += "Content-Tpe:text/html\r\n"  # 响应头
            response += "\r\n"
            response += fd.read()  # 响应体
        # 将请求的网页发送给浏览器
        connfd.send(response.encode())

    # 处理数据（在这个版本中，暂不做数据处理）
    def get_data(self, connfd, info):
        response = "HTTP/1.1 200 ok\r\n"
        response += "Content-Tpe:text/html\r\n"
        response += "\r\n"
        response += "Sorry not found" + info
        connfd.send(response.encode())


if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 8000
    DIR = "./static"

    # 需要用户自己确定的量，可以通过参数传入，这也是我们封装类的时候，经常用的一种方法
    httpd = HTTPServer(HOST, PORT, DIR)
    httpd.serve_forever()
