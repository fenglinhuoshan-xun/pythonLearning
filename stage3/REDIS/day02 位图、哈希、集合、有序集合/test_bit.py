import redis

r = redis.Redis(host='127.0.0.1', port=6379, password='123456')

r.setbit('pybit1', 4, 1)  # 0000 1000
print(r.getbit('pybit1', 3))  # 0
print(r.getbit('pybit1', 4))  # 1
print(r.bitcount('pybit1'))  # 1
