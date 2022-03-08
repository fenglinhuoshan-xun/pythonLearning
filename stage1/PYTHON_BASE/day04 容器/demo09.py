"""
    列表推导式嵌套
"""
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["咖啡", "牛奶", "雪碧", "可乐"]
# list03 = []
# for r in list01:
#     for c in list02:
#         list03.append(r + c)

list03 = [r + c for r in list01 for c in list02] # for循环与for循环之间有空格，表达式和for循环之间有间隔
print(list03)