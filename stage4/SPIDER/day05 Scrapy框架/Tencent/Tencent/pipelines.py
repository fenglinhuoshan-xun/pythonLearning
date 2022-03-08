# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from .settings import *
import pymongo


class TencentPipeline(object):
    def process_item(self, item, spider):
        print(item['job_name'], item['job_addr'], item['update_time'])
        return item


class TencentMongoPipeline(object):
    def open_spider(self, spider):
        self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        self.myset.insert_one(dict(item))

        return item
