"""
正则表达式函数
"""
import re

s = 'Alex:1999,Tom:1996'
pattern = r"(\w+):(\d+)"

# 使用re调用
l = re.findall(pattern, s)
print(l)

# compile对象
regex = re.compile(pattern)
l = regex.findall(s,0,13)
print(l)

# 使用正则表达式匹配到的内容切割字符串
l=re.split("[^\w+]",s)
print(l)

# 使用指定的字符串替换匹配到的内容
s = re.subn(r":","--",s)
print(s)

