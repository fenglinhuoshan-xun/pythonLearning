# -*- coding: utf-8 -*-
import scrapy
from ..items import BookfereItem


class BookfereSpider(scrapy.Spider):
    name = 'bookfere'
    allowed_domains = ['bookfere.com']
    i = 1
    start_urls = ['https://bookfere.com/post/category/books/weekly']

    def parse(self, response):
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

        # 生成下一页的地址，去交给调度器入队列
        if self.i < 5:
            self.i += 1
            url = 'https://bookfere.com/post/category/books/weekly/page/{}'.format(self.i)
            # 把url交给调度器入队列，callback：指响应对象对象回来了，交给哪个解析函数去处理
            yield scrapy.Request(url=url, callback=self.parse)
