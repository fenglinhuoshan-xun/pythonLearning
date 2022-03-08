"""
    猫眼电影top100数据抓取
"""

import requests
import re
import time
import random


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://www.maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': ''
        }
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
        item = {}
        for r in r_list:
            item['name'] = r[0].strip()
            item['star'] = r[1].strip()
            item['time'] = r[2].strip()
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
