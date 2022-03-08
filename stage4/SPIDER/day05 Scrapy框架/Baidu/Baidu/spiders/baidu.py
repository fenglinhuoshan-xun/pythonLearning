# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名，默认与爬虫文件名相同，我们可以自己改。执行爬虫时使用: scrapy crawl 爬虫名
    name = 'baidu'
    # 允许爬取的域名: scrapy genspider baidu www.baidu.com 其实如果创建爬虫文件时域名写错了，可以在这里改，但最后一次性写对
    allowed_domains = ['www.baidu.com']
    # 起始的url地址，默认在域名前面加上协议，后面加上/，我们可以改
    start_urls = ['http://www.baidu.com/']

    # 解析提取数据的函数
    def parse(self, response):
        """解析提取数据：百度一下，你就是知道"""
        item = {}
        # response.xpath()结果：[selector xpath='' data='xxx'>,<>,...]
        # extract()：把列表中的选择器对象序列化为unicode编码的字符串，即会将列表中所有的选择器对象中的字符串给提取出来。结果：['百度一下，你就是知道']
        # extract_first()：只序列化提取第一个选择器里面的字符串
        # get()：等同于extract_first()。1.5版本之前的必须用extract_first()，之后的可以用get()
        # item['title'] = response.xpath('/html/head/title/text()') # {'title': [<Selector xpath='/html/head/title/text()' data='百度一下，你就知道'>]}
        # item['title'] = response.xpath('/html/head/title/text()').extract()  # {'title': ['百度一下，你就知道']}
        # item['title'] = response.xpath('/html/head/title/text()').extract_first()  # {'title': ['百度一下，你就知道']}
        item['title'] = response.xpath('/html/head/title/text()').get()  # {'title': ['百度一下，你就知道']}
        print(item)
