# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 管道1：终端打印输出
class BookferePipeline(object):
    def process_item(self, item, spider):
        print(item['book_name'], item['book_time'])
        return item


# 管道2：把数据存入MySQL数据库
# 提前建库建表
# create database bookferedb charset urf8;
# use bookferedb;
# create table bookferetab(
# name varchar(200),
# time date,
# editor varchar(200),
# intr varchar(300),
# link varchar(200)
# )charset=utf8;

import pymysql
from .settings import *


class BookfereMysqlPipeline(object):
    def open_spider(self, spider):
        """爬虫程序开始时，只执行一次，一般用于数据库的连接"""
        # scrapy希望将变量定义到settings.py
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset=CHARSET)
        self.cur = self.db.cursor()
        print("我是open_spider函数")

    def process_item(self, item, spider):
        ins = 'insert into bookferetab values(%s,%s,%s,%s,%s)'
        li = [
            item['book_name'].strip(),
            item['book_time'].strip(),
            item['book_editor'].strip(),
            item['book_intr'].strip(),
            item['book_link'].strip()
        ]
        self.cur.execute(ins, li)
        # 千万不要忘记提交到数据库执行
        self.db.commit()

        # 假如你有多个管道，它会把上一个管道的返回值继续交由下一个管道处理，所有一定要有return item
        return item

    def close_spider(self, spider):
        """爬虫程序结束时，只执行一次，一般用于数据库的断开"""
        self.cur.close()
        self.db.close()
        print("我是close_spider函数")


# 管道3：存入MongoDB数据库管道
import pymongo


class BookfereMongodbPipeline(object):
    def open_spider(self, spider):
        """连接Mongodb"""
        self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[MYSQL_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        d = dict(item)  # 将item对象处理成一个字典
        self.myset.insert_one(d)

        return item
