"""
需求：
    输入贴吧名：
    输入起始页：
    输入终止页：
    最终把对应页面的html文件保存下来
思路：
    1. 右键 - 查看网页源代码，确认所抓取数据在响应内容中是否存在
    2. 发现存在！开始寻找URL地址规律
    3. 拼接URL地址，发送请求获取响应
    4. 数据解析处理
"""

import requests
from urllib import parse
import time, random


class BaiduSpider:
    def __init__(self):
        """定义常用变量"""
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'  # 打算使用quote编码
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

    def get_html(self, url):
        """请求的功能函数，获取响应内容html"""
        html = requests.get(url=url, headers=self.headers).content.decode('utf-8')
        return html

    def parse_html(self):
        """解析的功能函数，解析提取数据"""
        pass

    def save_html(self, filename, html):
        """数据处理的功能函数，把数据存入数据库，本地文件..."""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    def run(self):
        """程序入口函数，做整体的逻辑调控"""
        name = input('请输入贴吧名：')
        start = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        # 进行编码
        params = parse.quote(name)
        for page in range(start, end + 1):
            pn = (page - 1) * 50
            page_url = self.url.format(params, pn)
            # 调用请求功能函数
            html = self.get_html(url=page_url)
            # 调用保存功能函数
            filename = '{}_第{}页'.format(name, page)
            self.save_html(filename, html)
            # 终端提示
            print('第%d页抓取完成' % page)
            # 控制数据抓取的频率，每抓取1个页面，随机休眠一段时间
            time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    spider = BaiduSpider()
    spider.run()
