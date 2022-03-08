"""
将dict.txt文件中所有单词存入这个数据表
"""

import pymysql
import re

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 生成游标对象 (操作数据库,执行sql语句,获取结果)
cur = db.cursor()

f = open('dict.txt')
# 插入单词
args_list = []
for line in f:
    # 获取单词和解释
    # word,mean = line.split(' ',1)
    tup = re.findall(r"(\w+)\s+(.*)", line)[0]
    # args_list.append((word,mean.strip()))
    args_list.append(tup)

sql = "insert into words (word,mean) " \
      "values (%s,%s);"
try:
    cur.executemany(sql, args_list)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库连接
cur.close()
db.close()
