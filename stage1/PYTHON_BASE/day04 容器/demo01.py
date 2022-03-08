"""
    list --> str
"""
# 根据xx逻辑，拼接一个字符串
# range(10) --> "0123456789"

# str_result = "" # 不可变
# for item in range(10):
#     # str_result += str(item)
#     # 每次循环，每次拼接，都会创建新对象，产生一个垃圾
#     str_result = str_result + str(item)
# print(str_result)

list_temp = [] # 可变
for item in range(10):
    # 每次追加新对象，不会产生垃圾
    list_temp.append(str(item))
str_result = "-".join(list_temp)
print(str_result)