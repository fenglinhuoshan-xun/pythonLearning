import redis

import time

# 创建连接池并连接到redis
pool = redis.ConnectionPool(host='127.0.0.1', db=0, port=6379, password='123456')
r = redis.Redis(connection_pool=pool)

def withpipeline(r):
    """使用管道"""
    p = r.pipeline()

    for i in range(1000):
        key = 'test1' + str(i)
        value = i + 1
        p.set(key, value)

    p.execute()


def withoutpipeline(r):
    """没有使用管道"""
    for i in range(1000):
        key = 'test2' + str(i)
        value = i + 1

        r.set(key, value)


if __name__ == '__main__':
    t1 = time.time()
    withpipeline(r)  # time is 0.05308127403259277
    withoutpipeline(r)  # time is 0.18812823295593262
    t2 = time.time()

    print('time is %s' % (t2 - t1))
