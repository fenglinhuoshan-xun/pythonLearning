"""
功能标志位演示
"""

import re

s = """Hello
北京
"""
# print(s)

# 只匹配ASCII码
# regex = re.compile(r'\w+', flags=re.A)

# 匹配时不区分字母大小写
# regex = re.compile(r'[a-z]+', flags=re.I)

# 让.可以匹配到换行
# regex = re.compile(r'.+', flags=re.S)

# 让^ $ 可以匹配每一行的开头结尾
regex = re.compile(r'^北京', flags=re.M | re.I)
l = regex.findall(s)
print(l)
