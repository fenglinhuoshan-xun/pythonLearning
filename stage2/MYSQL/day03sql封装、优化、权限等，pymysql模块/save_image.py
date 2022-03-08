"""
存储二进制文件
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

# 存储图片
# sql = "update cls set img=%s where id = 1;"
# f = open('1.jpg', 'rb')  # 一定是读成字节串
# data = f.read()
# try:
#     cur.execute(sql, [data])
#     db.commit()
# except:
#     db.rollback()

# 获取图片
sql = "select img from cls where id=1;"
cur.execute(sql)
data = cur.fetchone()

with open('1.jpg','wb') as f:
    f.write(data[0])

# 关闭游标和数据库
cur.close()
