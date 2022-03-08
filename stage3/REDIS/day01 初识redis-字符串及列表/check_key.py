DB_NUMBERS = 16  # 数据库数量
KEY_NUMBERS = 20  # 每次检查key的数量，每次随机抽取的数量，看拿出来这些过没过期，如果拿出来的大部分都过期了，那继续拿

current_db = 0  # 记录当前检查到哪个库，是一个标记位，梅100ms主动扫描


# 核心的删除就是调用的这个方法，每100ms会调用这个方法
def activeExpireCycle():
    # 循环数据库，这个方法，有总的时间限制
    for i in range(DB_NUMBERS):

        if current_db == DB_NUMBERS:  # 周而复始
            current_db = 0

        # 获取当前数据库
        redisDB = server.db[current_db]  # 获取0库对应的数据库对象，是为了取数据用的
        first_start = True  # 标记当前第一次进行删除的一个标记位，只要是第一次执行删除，就是True
        del_key_num = 0  # 这一次删除key的数量
        current_db += 1

        # 根据while的条件判断，尽可能多的删除这个库中的数据

        while (first_start or del_key_num > KEY_NUMBERS / 4):
            first_start = False
            for j in range(KEY_NUMBERS):

                _key = redisDB.randomExpireKey()  # 随机拿key
                if is_expire(_key):
                    # 过期 则直接删除
                    delete_key(_key)
                    del_key_num += 1

                if time_is_limit():
                    # 若执行时间太长则返回， 默认25毫秒
                    return


