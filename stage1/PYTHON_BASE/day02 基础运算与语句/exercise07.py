"""
    先在终端中录入一个数字，
    再录入一个运算符
    最后录入一个数字
    打印计算的结果
    要求：如果运算符不是+ - * /　则提示"运算符输入有误"
"""
number_one = float(input("请输入第一个数字："))
operator = input("请输入一个运算符：")
number_two = float(input("请输入第二个数字："))
if operator == "+":
    print(str(number_one + number_two))
elif operator == "-":
    print(str(number_one - number_two))
elif operator == "*":
    print(str(number_one * number_two))
elif operator == "/":
    print(str(number_one / number_two))
else:
    print("运算符输入有误")
