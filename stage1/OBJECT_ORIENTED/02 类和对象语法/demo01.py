"""
    实例成员
        实例变量：
            对象.变量名称（当你想创建实例变量或者访问实例变量时，只要遵从这个语法就ok了）
"""


# 写法１：建议用这种
# class Wife():
#     def __init__(self, name="", face_score=0, age=0):
#         self.name = name
#         self.face_score = face_score
#         self.age = age
#
#     def play(self):
#         print(self.name, "玩耍")
#
#
# ak = Wife("阿珂", 100, 23)
# sq = Wife("苏荃", 92, 32)
# ak.play() # 通过对象地址调用实例方法，即自动的将对象地址传入到实例方法之中
# sq.play()


# 写法2：在其他语言中，这样的写法就是错误的。但是真正在实践中，不会这样写
# 类中要放什么样的数据，定义什么样的行为，由架构师决定
# 不建议这样写
class Wife():
    pass


ak = Wife()
# python允许我们在这个类的后面给这个对象添加实例变量
# 创建实例变量
ak.name = "阿珂"
# 读取实例变量
print(ak.name)


# 写法3：也不建议
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.fun01(age)

    def fun01(self, age=0):
        self.age = age


ak = Wife("阿珂", 23)
print(ak.name)
print(ak.age)

# 但凡是__开头__结尾的，都是系统定义的
# 在python中，如果想获取一个对象的所有的实例变量，可以用__dict__获取实例变量及对应的数据，以字典形式
print(ak.__dict__)
