"""
event 互斥方法
"""
from threading import Thread, Event
from time import sleep

e = Event()
s = None  # 全局变量，用于通信


def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()  # 结束wait阻塞


t = Thread(target=杨子荣)
t.start()

print("谁对口令才是自己人")
e.wait()  # 阻塞等待
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("自己人!")
else:
    print("打死他")

t.join()
