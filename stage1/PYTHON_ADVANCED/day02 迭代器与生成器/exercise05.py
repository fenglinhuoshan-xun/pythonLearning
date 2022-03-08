"""
    定义函数：在列表中获取所有偶数
        -- 传统思想：将结果存入新列表再返回
        -- 生成器思想：将结果交给生成器对象推算
    通过调试，体会惰性操作
"""
list01 = [43, 42, 68, 66, 78, 87, 453, 4]


def get_even01():
    list_result = []
    for item in list01:
        if item % 2 == 0:
            list_result.append(item)
    return list_result


result = get_even01()
for item in result:
    print(item)


# 如果一个函数内部有yield，则这个函数就叫做生成器函数，特点：就是你调它，它返回的是一个生成器对象，生成器对象，需要你再去for，就能拿到里面的数据了
def get_even01():
    for item in list01:
        if item % 2 == 0:
            yield item  # 当写一个yield的时候，这个函数就是一个生成器函数


# 生成器好处：要想返回数据，数据量再多，也不用担心内存不够用，因为用于接收数据的就是一个变量，每次只接收一个数据
# 返回生成器对象
result = get_even01()
for item in result:
    print(item)

# 什么时候用return，什么时候用yield？
# 指标：如果函数向外返回单个结果，就用return，如果函数想外返回多个结果，就用yield
