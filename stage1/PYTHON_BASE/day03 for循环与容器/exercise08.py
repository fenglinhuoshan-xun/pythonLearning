# 2. 在控制台中重复获取编码值，打印字符串，如果输入为空，则退出程序

while True:
    str_code = input("请输入编码值：")
    if str_code != "":
        str = chr(int(str_code))
        print(str)
    else:
        break
