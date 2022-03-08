"""
    从终端中输入搜索的关键字，保存html文件到本地（使用quote方法实现）
"""

import requests
from urllib import parse

# 1. 拼接URL地址
keyword = input('请输入关键字：')
params = parse.quote(keyword)
url = 'http://www.baidu.com/s?wd={}'.format(params)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

# 2. 发请求获取响应内容

html = requests.get(url=url, headers=headers).content.decode('utf-8')

# 3. 保存文件到本地
filename = '{}.html'.format(keyword)
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)
