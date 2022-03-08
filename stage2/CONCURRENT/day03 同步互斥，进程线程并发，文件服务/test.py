"""
线程的效率测试：对计算密集型程序和无阻塞的IO密集型程序分别使用单线程、多进程、多线程执行，测试其执行效率
"""


def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1


def io():
    write()
    read()


def write():
    f = open('test.txt', 'w')
    for i in range(1800000):
        f.write('Hello world\n')
    f.close()


def read():
    f = open('test.txt')
    f.readlines()
    f.close()
