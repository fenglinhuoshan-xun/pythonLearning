# -*- coding: utf-8 -*-
import scrapy
from ..items import BookfereItem


class BookfereSpider(scrapy.Spider):
    name = 'bookfere2'
    allowed_domains = ['bookfere.com']

    # 1. 删掉start_urls变量
    # 2. 重写start_requests()方法
    def start_requests(self):
        """一次性生成所有要抓取的url地址，一次性的交给调度器入队列"""
        for i in range(1, 6):
            url = 'https://bookfere.com/post/category/books/weekly/page/{}'.format(i)
            # 交给调度器入队列，并指定解析函数
            yield scrapy.Request(url=url, callback=self.detail_page)

    def detail_page(self, response):
        li_list = response.xpath('//*[@id="main"]/article')
        for li in li_list:
            item = BookfereItem()
            item['book_name'] = li.xpath('.//h1/a/text()').get()
            item['book_time'] = li.xpath('.//time[@class="entry-date published"]/text()').get()
            item['book_editor'] = li.xpath('.//a[@class="url fn n"]/text()').get()
            item['book_intr'] = li.xpath('./div[@class="entry-summary"]/p/text()').get()
            item['book_link'] = li.xpath('.//h1/a/@href').get()

            # 把抓取的数据提交给管道文件处理： yield item
            yield item
