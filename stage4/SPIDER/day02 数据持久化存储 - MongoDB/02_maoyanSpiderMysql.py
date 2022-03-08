"""
    猫眼电影top100数据抓取 -- 存入mysql数据库
"""

import requests
import re
import time
import random
import pymysql


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://www.maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'
        }
        # 数据库连接对象 + 游标对象，此过程只需要执行一次
        self.db = pymysql.connect('localhost', 'root', '123456', 'mydb', charset='utf8')
        self.cur = self.db.cursor()

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
        # r_list: [(),(),...]
        ins = 'insert into mytab values(%s,%s,%s)'
        for r in r_list:
            li = [
                r[0].strip(),
                r[1].strip(),
                r[2].strip(),
            ]
            self.cur.execute(ins, li)
            # 千万别忘了提交到数据库执行
            self.db.commit()
            print(li)

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            page_url = self.url.format(offset)
            self.get_html(url=page_url)
            # 控制抓取的频率
            # randint：生成指定范围内的整数
            # uniform：生成指定范围内的浮点数
            time.sleep(random.uniform(0, 1))

        # 一定要等所有页的数据抓取完成之后，再断开数据库连接
        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
