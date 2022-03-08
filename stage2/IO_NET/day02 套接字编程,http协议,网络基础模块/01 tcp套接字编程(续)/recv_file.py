from socket import *

s = socket()
s.bind(('127.0.0.1', 7777))
s.listen(3)

c, addr = s.accept()
print("Connect from:", addr)

# 接受思路： 1. wb写打开文件
#          2. recv 内容 write
# 打开文件
f = open('2.jpg', 'wb')

# 循环接受内容，写入文件
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()
