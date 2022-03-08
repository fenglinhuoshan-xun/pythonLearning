"""
    重写：覆盖
        子类具有和父类名称相同的方法
        调用子类对象时，执行子类方法（父类方法被覆盖，不执行），即子类方法可以任意写
"""


# 在开发过程中，我们还有很多可以内置的重写函数
# __str__：将对象 -->　字符串

# 我们任何一个类，都会直接或者间接的继承自object类
class Wife(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 你想打印出来什么风格，就可以重写__str__这个函数
    # 对象 -- 字符串（没有限制）
    def __str__(self):
        return "奴家%s今年%d岁啦" % (self.name, self.age)

    # 对象 -- 字符串（有限制，必须满足python语法）
    def __repr__(self):
        # return "Wife('双儿', 22)"  # 即就是将创建对象的语句放在双引号中，构成字符串的形式
        return "Wife('%s',%d)" % (self.name, self.age)  # 因为我们不能将数据写死，所有这样写


w01 = Wife("双儿", 22)
print(w01)


# print(w01)本质做的就是这件事，调用对象的__str__方法
content = w01.__str__()
print(content)

code = w01.__repr__()
print(code)

# eval：将字符串作为python代码执行
print(eval("1+2*3"))
# print(eval(input()))

# 拷贝（克隆）对象，eval配合__repr使用
w02 = eval(w01.__repr__())
# 对之前对象的修改不会影响克隆后的对象
w01.age = 26

print(w02.age)
