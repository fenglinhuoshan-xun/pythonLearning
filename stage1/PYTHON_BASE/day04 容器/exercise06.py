"""
    计算字符串中每个字符出现次数
    输入：abcbdeacb
    输出：
        字符a,2次
        字符b,3次
        字符c,2次
        字符d,1次
        字符e,1次
"""
str = "abcbdeacb"
dict_result = {}
for item in str:
    if item not in dict_result:
        dict_result[item] = 1
    else:
        dict_result[item] += 1
print(dict_result)

for k, v in dict_result.items():
    print("字符%s,%d次" % (k, v))
