"""
    猫眼电影top100数据抓取 -- 存入MongoDB数据库
    思路：
        1. 在__init__中创建相关对象
        2. 在save_html()中，把抓取的数据处理为字典，然后存入MongoDB数据库
"""

import requests
import re
import time
import random
import pymongo


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://www.maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'
        }
        # 创建3个对象
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['filmdb']
        self.myset = self.db['filmset']

    def get_html(self, url):
        """获取响应内容"""
        html = requests.get(url=url, headers=self.headers).content.decode('utf-8')
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析提取数据函数"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        pattern = re.compile(regex, re.S)
        # r_list: [('我不是药神','徐峥',2018-07-05),(),...]
        r_list = pattern.findall(html)
        # 直接调用数据处理函数
        self.save_html(r_list)

    def save_html(self, r_list):
        """具体数据处理的函数"""
        for r in r_list:
            # item创建到for循环的里面，不能放在for循环外面，否则会报主键错误
            item = {}
            item['name'] = r[0].strip()
            item['star'] = r[1].strip()
            item['time'] = r[2].strip()
            # 存入mongodb数据库
            self.myset.insert_one(item)
            print(item)

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            page_url = self.url.format(offset)
            self.get_html(url=page_url)
            # 控制抓取的频率
            # randint：生成指定范围内的整数
            # uniform：生成指定范围内的浮点数
            time.sleep(random.uniform(0, 1))


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
