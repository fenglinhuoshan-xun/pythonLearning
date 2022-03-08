"""
    在不改变原有功能的定义与调用情况下,为其增加新功能.
"""
import time


def print_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        print(stop_time - start_time)
        return result

    return wrapper


@print_execute_time
def func01():
    sum_value = 0
    for i in range(100):
        sum_value += i
    return sum_value


@print_execute_time
def func02(n):
    sum_value = 0
    for i in range(n):
        sum_value += i
    return sum_value


func01()

func02(100000)
