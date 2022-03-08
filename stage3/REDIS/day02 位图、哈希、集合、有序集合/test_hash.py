import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

r.hmset('pyh1', {'name': 'wwc', 'age': 60})
print(r.hgetall('pyh1'))  # {b'name': b'wwc', b'age': b'60'}
