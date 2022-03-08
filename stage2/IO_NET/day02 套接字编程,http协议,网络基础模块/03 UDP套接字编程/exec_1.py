"""
从终端输入一个单词
从单词本中找到该单词，打印解释内容
如果找不到，则打印“找不到”
"""

word = input("word:")  # 要查找的单词

# 默认r打开
f = open('dict.txt')

# 每次获取一行
for line in f:
    w = line.split(' ')[0]
    # 如果遍历到的单词已经大于word就结束查找
    if w > word:
        print("没有找到该单词")
        break
    elif w == word:
        print(line)
        break
else:
    print("没找到该单词")

f.close()
