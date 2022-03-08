"""
    正则表达式分组示例
"""
import re

html = 'A B C D'
pattern = re.compile('\w+\s+\w+', re.S)
r_list = pattern.findall(html)
print(r_list)
# 结果： ['A B', 'C D']

pattern = re.compile('(\w+)\s+\w+', re.S)
r_list = pattern.findall(html)
print(r_list)
# 第一步匹配：先匹配完整的模式 ['A B', 'C D']
# 第二步匹配：再去匹配子模式中的内容 ['A', 'C']，正则表达式中只要一个分组的话，结果为列表中每一项是字符串

pattern = re.compile('(\w+)\s+(\w+)', re.S)
r_list = pattern.findall(html)
print(r_list)
# 第一步匹配：['A B', 'C D']
# 第二步匹配：[('A', 'B'), ('C', 'D')]，正则表达式中如果有两个及两个以上的分组的时候，结果为列表中每一项为元组


