"""
    汽车之家二级页面数据抓取案例 -- 利用redis来实现增量爬虫
    思路：
        1. 一级页面提取数据：汽车详情页链接
        2. 二级页面提取数据：具体汽车的数据
        3. 建立User-Agent池来应对反爬虫
            fake_useragent模块
            sudo pip3 install fake_useragent
            from fake_useragent import UserAgent
            UserAgent().random

增量爬虫思路：
    1. 利用redis集合存储所有请求的指纹
    2. 利用sadd()方法的返回值来判断之前是否抓取过此请求
"""

import requests
import re
import time
import random
from fake_useragent import UserAgent
import redis
from hashlib import md5
import sys


class CarSpider:
    def __init__(self):
        self.url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1lto1csp{}exx0/'
        # 连接redis
        self.r = redis.Redis(host='localhost', port=6379, db=0, password=123456)

    def get_html(self, url):
        """功能函数1 -- 获取html"""
        headers = {'User-Agent': UserAgent().random}
        # 有时候网站会特意在响应内容中嵌入几个无法识别的字符，这时候，程序就会报异常，这也是网站反爬的一种手段
        # 假如程序抛出异常: Unicode Decode Error: gb2312 code cannot decode character \xxx
        # 解决方案: decode()方法添加 ignore 参数，表示忽略特殊字符
        html = requests.get(url=url, headers=headers).content.decode('gb2312', 'ignore')

        return html

    def re_func(self, regex, html):
        """功能函数2 -- 正则解析函数"""
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)

        return r_list

    def md5_url(self, url):
        """功能函数3 -- 生成指纹的函数"""
        s = md5()
        s.update(url.encode())

        return s.hexdigest()

    def parse_html(self, one_url):
        """程序逻辑函数"""
        one_html = self.get_html(url=one_url)
        one_regex = '<li class="cards-li list-photo-li ".*?<a href="(.*?)"'
        # href_list: ['','',...]
        href_list = self.re_func(regex=one_regex, html=one_html)
        for href in href_list:
            two_url = 'https://www.che168.com' + href
            # print(two_url)
            finger = self.md5_url(url=two_url)
            # 返回值为1：说明添加成功，说明之前没有抓取过此地址
            if self.r.sadd('car:spiders', finger) == 1:
                # 提取一辆汽车的具体信息
                self.get_car_info(two_url)
                # 控制抓取频率，每抓取一辆汽车，随机休眠0-1秒钟
                time.sleep(random.uniform(0, 1))
            else:
                # 一旦发现第一个已经抓取过的，说明后面的一定也抓过了，此时彻底结束程序
                sys.exit('更新完成，程序退出')

    def get_car_info(self, two_url):
        """提取一辆汽车的具体信息"""
        two_html = self.get_html(url=two_url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">&#165;(.*?)<b>万</b>'
        r_list = self.re_func(regex=two_regex, html=two_html)
        item = {}
        item['name'] = r_list[0][0].strip()
        item['km'] = r_list[0][1].strip()
        item['time'] = r_list[0][2].strip()
        item['type'] = r_list[0][3].split('/')[0].strip()
        item['displacement'] = r_list[0][3].split('/')[1].strip()
        item['address'] = r_list[0][4].strip()
        item['price'] = r_list[0][5].strip()
        print(item)

    def run(self):
        for o in range(1, 3):
            page_url = self.url.format(o)
            self.parse_html(one_url=page_url)


if __name__ == '__main__':
    spider = CarSpider()
    spider.run()

# 有时候，网站会给我们的响应内容和页面结构不一样，造成我们的正则写的不对，
# 这时候，要打印出网站的响应，根据实际响应来写正则才行，这也是网站的一种反爬机制
