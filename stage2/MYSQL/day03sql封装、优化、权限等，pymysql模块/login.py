"""
编写一个类，实例化对象时可以连接数据库，通过该对象调用方法可以模拟完成简单的登录注册功能
"""
import pymysql


class Database:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='stu',
                                  charset='utf8')

        # 生成游标对象 (操作数据库,执行sql语句,获取结果)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标和数据库连接
        self.cur.close()
        self.db.close()

    def register(self, name, passwd):
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        r = self.cur.fetchone()  # 如果有查询结果则name存在
        if r:
            return False
        # 插入数据库
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
        sql = "select * from user \
    where name='%s' and passwd='%s'" % (name, passwd)
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False


if __name__ == '__main__':
    db = Database()
    db.register('Tom', '123')
    db.login('Tom', '123')
    db.close()
