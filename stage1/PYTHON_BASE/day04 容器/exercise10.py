"""
    在控制台中循环录入内容，如果为空，则停止
    打印所有不重复的内容
"""
set_result = set()
while True:
    str_input = input("请输入：")
    if str_input == "":
        break
    set_result.add(str_input)
for item in set_result:
    print(item)