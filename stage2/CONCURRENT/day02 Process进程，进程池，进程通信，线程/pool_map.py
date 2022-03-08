from multiprocessing import Pool
from time import sleep


def fun(n):
    sleep(2)
    print("执行事件")
    return n * n


pool = Pool()

r = pool.map(func=fun, iterable=[1, 2, 3, 4, 5, 6])

pool.close()
pool.join()
print(r)  # [1, 4, 9, 16, 25, 36]
