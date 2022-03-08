"""
线程属性
"""
from threading import Thread
from time import sleep


def fun():
    for i in range(3):
        print("线程属性...")
        sleep(3)


t = Thread(target=fun, name='Tedu')

t.setDaemon(True)

t.start()

t.setName("Tarena")

print(t.is_alive())
print(t.name)
print(t.getName())
