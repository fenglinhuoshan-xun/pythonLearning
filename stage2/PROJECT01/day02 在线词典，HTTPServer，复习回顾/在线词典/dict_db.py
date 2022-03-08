"""
dict 数据处理
"""

import pymysql
import hashlib

# 对密码进行加密
def change_passwd(passwd):
    hash = hashlib.md5()
    hash.update(passwd.encode())
    return hash.hexdigest()


# 数据库处理类
class Database:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='123456',
                             database='dict',
                             charset='utf8')

    def create_cur(self):
        # 生成游标对象 (操作数据库,执行sql语句,获取结果)
        self.cur = self.db.cursor()

    def close(self):
        # 和数据库连接
        self.db.close()

    def register(self, name, passwd):
        sql = "select name from user where name='%s'" % name
        self.cur.execute(sql)
        r = self.cur.fetchone()  # 如果有查询结果则name存在
        if r:
            return False
        # 插入数据库
        passwd = change_passwd(passwd)
        sql = "insert into user (name,passwd) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

        # 登录处理

    def login(self, name, passwd):
        # 数据库查找
        passwd = change_passwd(passwd)
        sql = "select * from user \
    where name='%s' and passwd='%s'" % (name, passwd)
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

    def query(self, word):
        sql = "select mean from words where word='%s'" % word
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return r[0]

    def insert_history(self, name, word):
        sql = "insert into hist (name,word) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except Exception:
            self.db.rollback()

    def history(self, name):
        sql = "select name,word,time from hist \
            where name='%s' \
            order by time desc limit 10" % name
        self.cur.execute(sql)
        return self.cur.fetchall()