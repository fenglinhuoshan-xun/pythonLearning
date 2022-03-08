"""
向京东官网发起请求，并得到响应
"""
import requests

# 1. get()方法获取到的为响应对象，响应对象里面都是属性，没有方法
resp = requests.get(url='https://www.jd.com/')
print(resp)  # <Response [200]>
# 2. text属性：获取响应对象的内容 -- 字符串形式（右键->查看网页源代码）
html = resp.text
# 3. content属性：获取响应内容 -- 字节串形式。在抓取一些图片，文件，音频，视频的时候，就可以用这个
html = resp.content
# 4. status_code属性：获取HTTP响应吗
code = resp.status_code
print(code)  # 200
# 5. url属性：获取返回实际数据的URL地址
url = resp.url
print(url)  # https://www.jd.com/
