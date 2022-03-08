"""
    抓取有道翻译的翻译结果
    1. F12抓包，页面中翻译单词
    2. 分析Form表单数据变化
    3. 寻找加密的JS文件，并分析加密算法
    4. 用python实现对应的加密算法
    5. 处理headers、data为字典，发请求进行数据抓取
"""
import requests
import time
import random
from hashlib import md5
import json


class YdSpider:
    def __init__(self):
        self.post_url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        # Cookie，Referer，USer-Agent是网站检查频率最高的三个字段，其实只写这三个也可以
        self.headers = {
            '''Accept''': '''application/json, text/javascript, */*; q=0.01''',
            '''Accept-Encoding''': '''gzip, deflate, br''',
            '''Accept-Language''': '''zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7''',
            '''Connection''': '''keep-alive''',
            '''Content-Length''': '''252''',
            '''Content-Type''': '''application/x-www-form-urlencoded; charset=UTF-8''',
            '''Cookie''': '''OUTFOX_SEARCH_USER_ID=-889554401@240e:358:1305:c500:ad8c:d597:fdd9:9c9; OUTFOX_SEARCH_USER_ID_NCOO=1956310466.3207705; JSESSIONID=aaauzsBEBZQ6-7uo4br1x; ___rl__test__cookies=1637743975533''',
            '''Host''': '''fanyi.youdao.com''',
            '''Origin''': '''https://fanyi.youdao.com''',
            '''Referer''': '''https://fanyi.youdao.com/''',
            '''sec-ch-ua''': '''"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"''',
            '''sec-ch-ua-mobile''': '''?0''',
            '''sec-ch-ua-platform''': '''"Windows"''',
            '''Sec-Fetch-Dest''': '''empty''',
            '''Sec-Fetch-Mode''': '''cors''',
            '''Sec-Fetch-Site''': '''same-origin''',
            '''User-Agent''': '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36''',
            '''X-Requested-With''': '''XMLHttpRequest''',
        }

    def get_ts_salt_sign(self, word):
        # ts salt sign
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        string = "fanyideskweb" + word + salt + "Y2FYu%TNSbMCxc3t2u^XT"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts, salt, sign

    def attack_yd(self, word):
        # 获取ts salt sign
        ts, salt, sign = self.get_ts_salt_sign(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,  # 经验证，检查了salt和sign，没有检查lts和bv，这也是后期很重要的东西，salt：语言
            "sign": sign,  # sign：签名
            "lts": ts,
            "bv": "c795a332c678d5063a1ee5eb15253848",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        # html = requests.post(url=self.post_url, headers=self.headers,
        #                      data=data).text  # 字符串类型 {"translateResult":[[{"tgt":"hello","src":"你好"}]],"errorCode":0,"type":"zh-CHS2en"}
        # .json()：把json格式的字符串转为python数据类型，一个字典
        html = requests.post(url=self.post_url, headers=self.headers, data=data).json()
        # html = json.loads(html)
        result = html['translateResult'][0][0]['tgt']
        return result

    def run(self):
        word = input("请输入要翻译的单词：")
        result = self.attack_yd(word)
        print(result)


if __name__ == '__main__':
    spider = YdSpider()
    spider.run()
