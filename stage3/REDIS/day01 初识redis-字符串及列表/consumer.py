import redis
import json

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

# 消费者要监控任务队列，有没有我能做的事情
while True:
    task = r.brpop('pyl2', 10)  # 注意，一定要用阻塞式的
    print(task)  # (b'pyl2', b'{"task": "send_email", "email_body": "aaa", "from": "bbb", "to": "gxn"}')
    if task:
        json_obj = json.loads(task[1])
        # 具体任务执行逻辑
    else:
        print('---no task---')
