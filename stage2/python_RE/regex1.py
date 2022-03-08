"""
正则表达式函数演示２
"""
import re

# 匹配目标字符串得到迭代对象
s = "  1949年10月1日，中华人民共和国成立"

it = re.finditer(r'\d+', s)

for i in it:
    print(i.group())

# 匹配开头位置
obj = re.match(r"\d+", s)
print(obj)

# 匹配第一处
obj = re.search(r'\d+',s)
print(obj)

# 完全匹配
obj = re.fullmatch(r'.+',s)
print(obj)

