# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookfereItem(scrapy.Item):
    # define the fields for your item here like:
    # 书名，时间，作者，简介，链接
    book_name = scrapy.Field()
    book_time = scrapy.Field()
    book_editor = scrapy.Field()
    book_intr = scrapy.Field()
    book_link = scrapy.Field()

# 相当于你定义了一个字典，只给了key，没有给value
# {'name':'','time':'',...}
# 将爬虫得到的数据赋值给这些类变量
