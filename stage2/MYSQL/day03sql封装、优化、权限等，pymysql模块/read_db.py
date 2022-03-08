"""
mysql读操作演示
"""

import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user="root",
                     password='123456',
                     database='stu',
                     charset='utf8'
                     )

# 生成游标 （游标对象用于执行sql语句，获取执行结果）
cur = db.cursor()

# 对数据读操作
sql = "select name,age,score from cls where score > %s;"
cur.execute(sql, [80])

# 通过迭代游标对象获取查询结果
# for i in cur:
#     print(i)

# 利用函数获取查询结果
# 如果上面把所有结果都获取完了，则下面获取不到，因为迭代有一个过程，取完了就没有了
# one = cur.fetchone()
# print(one)

# many = cur.fetchmany(2)
# print(many)

all = cur.fetchall()
print(all)

# 关闭游标和数据库
cur.close()
db.close()
