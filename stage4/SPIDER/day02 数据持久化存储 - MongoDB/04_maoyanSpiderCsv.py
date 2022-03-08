"""
    猫眼电影top100数据抓取 -- 存入csv文件
"""

import requests
import re
import time
import random
import csv


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://www.maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'
        }
        # 打开文件和创建csv文件写入对象只需要执行一次
        # 问题1：windows中csv文件会多出空行，使用newline参数解决，windows中newline参数默认为\n，linux中newline参数默认为空
        # 问题2：gbk编码识别不了某些特殊字符，可以手动去指定字符编码
        self.f = open('maoyan.csv', 'w', newline='', encoding='gb18030')
        self.writer = csv.writer(self.f)

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
            li = [
                r[0].strip(),
                r[1].strip(),
                r[2].strip(),
            ]
            self.writer.writerow(li)
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

        # 所有页的数据抓取完成后，关闭文件
        self.f.close()


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
