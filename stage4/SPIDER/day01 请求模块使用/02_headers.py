"""
    向测试网站发请求，获取响应内容来确定User_Agent到底是什么？
"""
import requests

url = 'http://httpbin.org/get'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
html = requests.get(url=url, headers=headers).text
print(html)
