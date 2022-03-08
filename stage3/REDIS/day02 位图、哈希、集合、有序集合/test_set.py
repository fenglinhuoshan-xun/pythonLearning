import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

# r.sadd('pys1', 'a', 'b', 'c', 'd')
# print(r.smembers('pys1'))  # {b'c', b'b', b'd', b'a'}

r.sadd('pys2', 'a', 'f', 'c', 'z')
print(r.sinter('pys1', 'pys2'))  # {b'a', b'c'}

#######################################################################
r.zadd('pyz1', {'tom': 6000, 'jim': 8000, 'jack': 12000})

# [(b'tom', 6000.0), (b'jim', 8000.0), (b'jack', 12000.0)]
print(r.zrange('pyz1', 0, -1, withscores=True))  # 希望给出元素的分之，就将withscores设置为True，默认为False

print(r.zcount('pyz1', 800, 10000))  # 2
print(r.zcount('pyz1', "(8000", "(10000"))  # 0

r.zadd('pyz2', {'tom': 4000, 'jim': 6000})
# 不加权重，用元组
r.zinterstore('pyz3', ('pyz1', 'pyz2'), aggregate='max')
print(r.zrange('pyz3', 0, -1, withscores=True))  # [(b'tom', 6000.0), (b'jim', 8000.0)]

# 加了权重，用字典
r.zinterstore('pyz4', {'pyz1': 0.5, 'pyz2': 1}, aggregate='max')
print(r.zrange('pyz4', 0, -1, withscores=True))  # [(b'tom', 4000.0), (b'jim', 6000.0)]
