"""
    字符串字面值
"""
name01 = "悟空"
name02 = '悟空'

# 三引号：所见即所得，写什么样就是什么样，写什么格式就是什么格式
name03 = '''
    悟
空
'''
print(name03)
name04 = """悟空"""
message = '我是"齐天大圣"孙悟空.'
message = "我是'齐天大圣'孙悟空."
message = '''我是'齐天大圣'"孙悟空".'''
print(message)

# 转义符：为了避免冲突，改变原有含义的特殊字符。只是在代码层面去写的，输出来的东西就是它的原始字符串
# \" \' 水平制表格\t 换行\n \\
message = "我是\"齐天\n大圣\"孙\t悟空"
print(message)

url = "c:\\a\\b\c\d\\a.txt"
print(url)

# 用r标记的字符串：叫做原始字符串（表示字符串中没有转义符）
url = r"c:\a\b\c\d\a.txt"
print(url)

# 格式化字符串

# "..%d...%s....%f..."%(整数变量,字符串变量,小数变量)
# 1 + 2 = 3
number_one = 1
number_two = 2
str_result = "%d + %d = %d" % (number_one, number_two, number_one + number_two)
print(str_result)

name = "张无忌"
age = 25
score = 95.5
print("我叫%s今年%d岁了,考试%.f。" % (name,age,score))

