"""
    多继承
        继承：统一概念/隔离变化
        同名方法解析顺序 mro
"""


# mro:先执行自己，再执行父类，再执行爷爷类

class A:
    def func(self):
        print("A")


class B(A):
    def func(self):
        print("B")


class C(A):
    def func(self):
        print("C")


class D(B, C):
    def func(self):
        print("D")
        super().func()  # ? B
        C.func(self)  # 调用指定名称的父类的同名方法。即父类名称去点父类方法即可


d01 = D()
d01.func()

print(D.mro())  # 观察先执行哪个
