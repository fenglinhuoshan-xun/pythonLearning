"""
    Ajax动态加载数据 -- 豆瓣电影分类排行榜剧情片
    1. 右键，查看网页源代码，确认为动态加载行为
    2. F12抓包，页面执行点击行为
    3. XHR中查找返回数据数据的网络数据包 -- Preview
    4. 多次点击下一页，分析查询参数的变化 -- QueryString Paramters
"""

import requests
import json
import random
from fake_useragent import UserAgent
import time


class DouBanMovieSppider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).text
        # json.loads()：把json格式的字符串转为python数据类型
        html = json.loads(html)
        # 开始进行数据的解析提取
        self.parse_html(html)

    def parse_html(self, html):
        """数据解析提取"""
        for one_movie_dict in html:
            item = {}
            item['name'] = one_movie_dict['title']
            item['type'] = one_movie_dict['types']
            item['link'] = one_movie_dict['url']
            item['score'] = one_movie_dict['score']
            item['regions'] = one_movie_dict['regions']
            print(item)

    def run(self):
        for i in range(40):
            page_url = self.url.format(i)
            self.get_html(url=page_url)
            # 控制数据抓取的频率
            time.sleep(random.uniform(1, 3))


if __name__ == '__main__':
    spider = DouBanMovieSppider()
    spider.run()
