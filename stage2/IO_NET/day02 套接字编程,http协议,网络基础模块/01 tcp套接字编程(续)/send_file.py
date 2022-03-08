# 练习：将一个文件从客户端发送到服务端保存
#       * 文件可能是文本类型也可能是二进制类型
from socket import *

s = socket()
s.connect(('127.0.0.1', 7777))

# 读取目标文件，循环发送
f = open('1.jpg', 'rb')
while True:
    # 边读取，边发送
    data = f.read(1024)
    if not data:
        break
    s.send(data)

f.close()
s.close()
