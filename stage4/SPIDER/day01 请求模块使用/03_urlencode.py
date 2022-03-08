"""
    从终端中输入搜索的关键字，保存html文件到本地
"""

import requests
from urllib import parse

# 1. 拼接URL地址
keyword = input('请输入关键字：')
params = parse.urlencode({'wd': keyword})
url = 'http://www.baidu.com/s?{}'.format(params)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

# 2. 发请求获取响应内容
# html = requests.get(url=url, headers=headers).text  # 当我们用requests模块向网站发请求的时候，每一个网站都会有它自己的字符编码
# resp = requests.get(url=url, headers=headers)
# print(resp.encoding)  # 打印编码格式，ISO-8859-1，这个是requests模块猜测的编码格式，并不是网站真正给我们的响应内容的编码格式
html = requests.get(url=url, headers=headers).content.decode('utf-8')  # 要使用content.decode('utf-8')来保证不乱码

# 3. 保存文件到本地
filename = '{}.html'.format(keyword)
with open(filename, 'w', encoding='utf-8') as f:  # 在windows中打开一个文件，默认以GBK格式打开，会报错，在Linux当中，默认utf-8编码。可以用encoding来指定编码格式
    f.write(html)
