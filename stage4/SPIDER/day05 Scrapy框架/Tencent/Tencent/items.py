# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称：job_name
    # 职位地址：job_addr
    # 发布时间：update_time
    # 工作职责：responsibility
    # 工作要求：requirement

    job_name = scrapy.Field()
    job_addr = scrapy.Field()
    update_time = scrapy.Field()
    responsibility = scrapy.Field()
    requirement = scrapy.Field()
