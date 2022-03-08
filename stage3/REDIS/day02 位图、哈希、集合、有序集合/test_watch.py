import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', db=0, port=6379, password='123456')
r = redis.Redis(connection_pool=pool)


def double_account(user_id):
    key = 'account_%s' % (user_id)
    with r.pipeline(transaction=True) as pipe:
        while True:
            try:
                pipe.watch(key)  # 流水线点任何命令都暂时不发出去，唯独watch命令除外，watch命令会立即发送给redis服务端
                value = int(r.get(key))
                value *= 2
                print('sleep is start')
                time.sleep(15)
                print('sleep--is end')
                pipe.multi()
                pipe.set(key, value)
                pipe.execute()  # 如果在失误提交过程中，有别人改了被监听的数据，则会报一个WatchErro的错误，不像在redis终端里，事物提交错误，会反你一个nil
                break
            except redis.WatchError:
                print('---key changed')
                continue

    return int(r.get(key))


if __name__ == '__main__':
    print(double_account('guoxiaonao'))
