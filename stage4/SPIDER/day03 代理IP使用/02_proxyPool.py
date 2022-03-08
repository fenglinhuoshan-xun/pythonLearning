"""
    抓取快代理免费高匿代理，并测试，建立自己的代理IP池
"""

import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent


class ProxyPool:
    def __init__(self):
        self.url = 'https://www.kuaidaili.com/free/inha/{}/'
        # 测试的url地址
        self.test_url = 'http://httpbin.org/get'

    def get_proxy(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).text
        # 解析提取代理IP
        p = etree.HTML(html)
        # tr_list: [<element tr at xxx>,<>,...]
        tr_list = p.xpath('//tbody/tr')
        for tr in tr_list:
            ip_list = tr.xpath('./td[1]/text()')
            ip = ip_list[0].strip() if ip_list else None
            port_list = tr.xpath('./td[2]/text()')
            port = port_list[0].strip() if port_list else None
            # 测试此ip和port是否可用
            self.test_proxy(ip, port)

    def test_proxy(self, ip, port):
        """测试一个代理IP是否可用"""
        proxies = {
            'http': 'http://{}:{}'.format(ip, port),
            'https': 'https://{}:{}'.format(ip, port),
        }
        try:
            # 如果代理IP不能用，程序就会卡在这，所以设置timeout，
            resp = requests.get(url=self.test_url, proxies=proxies, timmeout=3)
            if resp.status_code == 200:
                print(ip, port, '\033[31m可用\033[0m')  # 将标准输出，设置为红色输出
            else:
                print(ip, port, '不可用')
        except:
            print(ip, port, '不可用')

    def run(self):
        for pg in range(1, 100):
            page_url = self.url.format(pg)
            self.get_proxy(url=page_url)
            # 控制数据抓取的频率
            time.sleep(random.uniform(2, 4))


if __name__ == '__main__':
    spider = ProxyPool()
    spider.run()
