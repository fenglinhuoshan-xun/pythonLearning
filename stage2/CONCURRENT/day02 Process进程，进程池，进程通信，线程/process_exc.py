"""
分别求证使用4个进程和10个进程计算100000以内质数之和的时间，与单进程时间比较，看是否提高了运行效率
"""
import multiprocessing
import time


def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("%s函数运行时间：%.8f" % (f.__name__, end_time - start_time))
        return res

    return wrapper


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True


def ifprime(i):
    if isPrime(i):
        return True


@timeit
def no_multi_process():
    prime = []
    for i in range(1, 100001):
        if ifprime(i):
            prime.append(i)
    sum(prime)


class prime2(multiprocessing.Process):
    def __init__(self, prime, begin, end):
        super().__init__()
        self.prime = prime
        self.begin = begin
        self.end = end

    def run(self):
        for i in range(self.begin, self.end):
            if ifprime(i):
                self.prime.append(i)
        sum(self.prime)


@timeit
def use_multi_process():
    prime = []
    processes = []
    for i in range(1, 100001, 25000):
        p = prime2(prime, i, i + 25000)
        p.start()
        processes.append(p)
    [process.join() for process in processes]


@timeit
def use10_multi_process():
    prime = []
    processes = []
    for i in range(1, 100001, 10000):
        f = prime2(prime, i, i + 10000)
        f.start()
        processes.append(f)
    [process.join() for process in processes]


if __name__ == '__main__':
    # no_multi_process() # 27.98723698
    # use_multi_process() # 16.78142691
    use10_multi_process()  # 17.07275319，并不是进程越多，效率越高，因为cpu内核数量是一定的
