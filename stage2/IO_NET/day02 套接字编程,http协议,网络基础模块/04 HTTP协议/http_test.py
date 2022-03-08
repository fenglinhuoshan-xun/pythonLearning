"""
http测试
"""

from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8000))
s.listen(3)

c, addr = s.accept()
print("Connect from", addr)

data = c.recv(2048)
print(data.decode())

# 注意：这里用的三引号，所以结尾换行直接按回车即可。如果用的双引号的话，记得结尾要用\r\n来换行
data = """HTTP/1.1 200 ok 
Content-Type:text/html

<h1>hello world</h1>
"""

c.send(data.encode())

c.close()
s.close()
