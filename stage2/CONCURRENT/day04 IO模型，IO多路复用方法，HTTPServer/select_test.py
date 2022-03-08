"""
select 方法示例
"""
from socket import *
from select import select
from time import sleep

s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(3)

f = open('test', 'r')

# 监控IO
print("监控IO")
sleep(5)
rs, ws, xs = select([s, f], [f], [])
print(rs)
print(ws)
print(xs)
