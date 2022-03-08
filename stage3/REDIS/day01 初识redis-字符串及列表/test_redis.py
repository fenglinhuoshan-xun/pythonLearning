import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0, password=123456)

#### 基础命令
# key_list = r.keys('*')
# print(key_list)  # [b'uuname', b'k1', b'k2', b'uuuname',  b'k3',  b'n1', b'l1',  b'l2']。默认返回的是数组，里面是字节串
# print(r.type('l1'))  # b'list'

##### list #####
# r.lpush('pyl1', 'a', 'v', 'w', 'z')
# print(r.lrange('pyl1', 0, -1))  # [b'z', b'w', b'v', b'a']
r.linsert('pyl1', 'before', 'v', 'g')
print(r.lrange('pyl1', 0, -1))

#### string ####
r.set('puname', 'guoxiaonao', ex=30)
print(r.get('puname'))
r.mset({'k1': 'v1', 'k2': 'v2'})
print(r.mget('k1', 'k2', 'k3', 'k6'))  # [b'v1', b'v2', b'v3', None]
