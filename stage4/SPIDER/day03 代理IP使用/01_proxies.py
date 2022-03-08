"""
    免费代理IP使用
"""

import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent': 'Mozilla/5.0'}
proxies = {
    # 免费的代理IP大多都不能用
    'http': 'http://125.108.106.105:9000',
    'https': 'https://121.13.252.61:41564',
}

# 测试
html = requests.get(url=url, proxies=proxies, headers=headers).text
print(html)
