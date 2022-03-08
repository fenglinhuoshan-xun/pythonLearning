"""
    在终端中循环录入字符串，如果输入为空则停止
    最后打印所有的内容（拼接后的字符串）
"""
list_temp = []
while True:
    str_input = input("请输入内容：")
    if str_input == "":
        break
    list_temp.append(str_input)
str_result = "".join(list_temp)
print(str_result)

