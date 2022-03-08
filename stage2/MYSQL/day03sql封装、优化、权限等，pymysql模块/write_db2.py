"""
数据库写操作
"""

import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user="root",
                     password="123456",
                     database='stu',
                     charset='utf8',
                     )

# 生成游标（游标对象主要用于执行sql语句，获取执行结果）
cur = db.cursor()

# 写数据库
# name = input("Name:")
# age = input("Age:")
# score = input("Score:")

data = [('zhang', 11, 55),
        ('li', 10, 56),
        ('wang', 10, 57)
        ]

try:
    # sql = "insert into cls (name,age,score) values ('%s',%s,%s);" % (name, age, score)
    # sql = "insert into cls (name,age,score) values (%s,%s,%s);"
    # print(sql)  # 插入数据时，一定要注意字符串类型的数据
    # cur.execute(sql, [name, age, score]) # 这块不用管数据类型，它会自动判定数据类型，自动转换

    sql = "insert into cls (name,age,score) values (%s,%s,%s);"
    # for i in data:
    #     cur.execute(sql,i)
    cur.executemany(sql, data)  # 一般用于执行大量的，相同的，重复的操作

    db.commit()  # 将操作提交，注意提交是用数据库进行提交
except Exception as e:
    print(e)
    db.rollback()  # 数据回滚，让数据变回到没有执行语句前的状态

# 关闭游标和数据库
cur.close()
db.close()
