"""
    豆瓣图书top250数据抓取 -- lxml + xpath
"""
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent


class DoubanBookSpider:
    def __init__(self):
        self.url = 'https://book.douban.com/top250?start={}'

    def get_html(self, url):
        """请求函数 -- 获取html"""
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析函数 -- 解析提起数据"""
        parse = etree.HTML(html)
        # table_list: [<element table at xxx>,<>,...]
        table_list = parse.xpath('//table')
        for table in table_list:
            item = {}
            # 千万不要贸然去取下标索引，要进行判断，否则有一个没数据，就会报错，阻碍其他数据抓取
            # 书的名称
            name_list = table.xpath('.//div[@class="pl2"]/a/text()')
            item['name'] = name_list[0].strip() if name_list else None
            # 书的描述
            comment_list = table.xpath('.//p[@class="pl"]/text()')
            item['comment'] = comment_list[0].strip() if comment_list else None
            # 书的评分
            score_list = table.xpath('.//span[@class="rating_nums"]/text()')
            item['score'] = score_list[0].strip() if score_list else None
            # 评论人数
            number_list = table.xpath('.//span[@class="pl"]/text()')
            item['number'] = number_list[0][1:-1].strip() if number_list else None
            # 书的说明
            instructions_list = table.xpath('.//span[@class="inq"]/text()')
            item['instructions'] = instructions_list[0].strip() if instructions_list else None
            print(item)

    def run(self):
        for page in range(1, 11):
            start = (page - 1) * 25
            page_url = self.url.format(start)
            self.get_html(page_url)
            # 控制数据抓取的频率
            time.sleep(random.uniform(0, 1))


if __name__ == '__main__':
    spider = DoubanBookSpider()
    spider.run()
