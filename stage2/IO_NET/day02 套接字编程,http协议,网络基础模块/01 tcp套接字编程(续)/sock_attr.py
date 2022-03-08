"""
套接字属性
"""

from socket import *

s = socket()

# 注意：这句话，必须在bind之前完成。表示程序结束之后，我们套接字绑定的端口，会立即被释放
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)

s.bind(('127.0.0.1', 8889))
s.listen(3)

print(s.family)
print(s.type)
print(s.getsockname())

c, addr = s.accept()
print(c.getpeername())
c.recv(1024)
