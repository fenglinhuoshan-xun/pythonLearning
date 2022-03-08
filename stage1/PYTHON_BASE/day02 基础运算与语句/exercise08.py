"""
    在终端中依次录入四个同学的体重，打印最重的值
    思路:
        假设第一个就是最大的
        使用假设的依次与后几个变量进行比较，如果发现更大的，则替换假设的
    输入：52、40、37、60
    输出：60
"""
number_one = float(input("请输入第一个同学的体重："))
number_two = float(input("请输入第二个同学的体重："))
number_three = float(input("请输入第三个同学的体重："))
number_four = float(input("请输入第四个同学的体重："))
max_value = number_one
if max_value < number_two:
    max_value = number_two
if max_value < number_three:
    max_value = number_three
if max_value < number_four:
    max_value = number_four
print(max_value)
