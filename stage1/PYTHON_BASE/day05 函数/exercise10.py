"""
    对字符串："  自强不 息,  厚德 载物. "
    查找空格数量
    删除所有空格
    查找"厚德"位置
    判断是否以"自强开头"
"""
message = "  自强不 息,  厚德 载物. "
print(message.count(" "))
print(message.replace(" ", ""))
print(message.find("厚德"))
print(message.startswith("自强"))

