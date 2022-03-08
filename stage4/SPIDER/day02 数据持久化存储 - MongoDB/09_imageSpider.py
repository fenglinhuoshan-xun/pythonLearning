"""
    抓取图片到本地
    思路：
        一定要找到图片的真实完整的url地址
"""
import requests
from fake_useragent import UserAgent

url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fww3.sinaimg.cn%2Fmw690%2F006jCXQuly1gw4ei15nblj329935s1kz.jpg&refer=http%3A%2F%2Fwww.sina.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1639647390&t=ea5826606390f54fb47c1976467ee771'
headers = {'User-Agent': UserAgent().random}

# 一定要使用content属性，因为图片是以二进制的方式存储的
html = requests.get(url=url, headers=headers).content

# 保存图片到本地
with open('girl.jpg', 'wb') as f:
    f.write(html)
