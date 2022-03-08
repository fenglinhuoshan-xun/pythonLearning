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

# 写数据库（写操作是要修改数据库，要慎重，一般加上try判断，一旦sql语句写错了，
# 或者是数据库不允许修改，就会产生异常，这时候可以执行回滚）
try:
    # sql = "insert into cls values (6,'Alex',10,'m',83);"
    # cur.execute(sql)
    sql = "update cls set score = 77.5 where id = 1;"
    cur.execute(sql)
    sql = "delete from cls where id = 6;"
    cur.execute(sql)
    db.commit()  # 将操作提交，注意提交是用数据库进行提交
except Exception as e:
    db.rollback() # 数据回滚，让数据变回到没有执行语句前的状态
"""
当整个程序执行完毕后，写的内容就生效了，但是如果当我们写这个数据外，后续还有其他大量操作，
可能一时半会儿不会执行close，则这个写操作不会立马生效，而是暂时放在缓存区里，
如果我们想要让它立即生效，我们可以用commit提交
"""


# 关闭游标和数据库
cur.close()
db.close()
