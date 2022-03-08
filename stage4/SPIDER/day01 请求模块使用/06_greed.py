"""
    贪婪匹配和非贪婪匹配演示
"""

import re

html = '''
<div><p>如果你为门中弟子伤她一分，我便屠你满门</p></div>
<div><p>如果你为天下人损她一毫，我便杀尽天下人</p></div>
'''
# 贪婪匹配，普通字符会一直匹配到最后一个</p></div>
pattern = re.compile('<div><p>.*</p></div>', re.S)
r_list = pattern.findall(html)
print(r_list)  # ['<div><p>如果你为门中弟子伤她一分，我便屠你满门</p></div>\n<div><p>如果你为天下人损她一毫，我便杀尽天下人</p></div>']

# 非贪婪匹配，普通字符会匹配到一个</p></div>就停止匹配
pattern = re.compile('<div><p>.*?</p></div>', re.S)
r_list = pattern.findall(html)
print(r_list)  # ['<div><p>如果你为门中弟子伤她一分，我便屠你满门</p></div>', '<div><p>如果你为天下人损她一毫，我便杀尽天下人</p></div>']

pattern = re.compile('<div><p>(.*?)</p></div>', re.S)
r_list = pattern.findall(html)
print(r_list)  # ['如果你为门中弟子伤她一分，我便屠你满门', '如果你为天下人损她一毫，我便杀尽天下人']
