"""
练习3：在终端中首先获取一个变量，再获取一个变量，然后交换变量
      最后输出两个变量
"""
variable01 = input("请输入第一个变量：")
variable02 = input("请输入第二个变量：")
# 变量交换思想：相当于你把你的东西放桌子上，我一拿，然后我把我的东西给你。
# 对于任何编程语言来说，都可以这样交换变量
# temp = variable01
# variable01 = variable02
# variable02 = temp

# python中还有更简单的写法
variable01, varialbe02 = variable02, variable01

print("第一个变量是：" + variable01)
print("第二个变量是：" + variable02)
