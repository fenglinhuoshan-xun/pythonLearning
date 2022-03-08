import redis
import json

r = redis.Redis(host='127.0.0.1', port=6379, db=0,
                password='123456')  # 你在redis视图中，可以在input redis之后呢，给出这样一个全局变量，把redis的链接初始化出来

# 把任务给消费者描述清楚
json_obj = {'task': 'send_email', 'email_body': 'aaa', 'from': 'bbb', 'to': 'gxn'}
json_str = json.dumps(json_obj)  # 将字典转化为json串
r.lpush('pyl2', json_str)
