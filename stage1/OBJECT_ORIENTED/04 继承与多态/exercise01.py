"""
    定义父类
        动物(行为：吃)
    定义子类
        狗(行为：)
        鸟(行为：飞)
    体会isinstance/issubclass/type
"""


class Animal:
    def eat(self):
        print("吃饭饭喽")


class Dog(Animal):
    def run(self):
        print("跑喽")
        super().eat()


class Bird(Animal):
    def fly(self):
        print("飞喽")
        super().eat()


d01 = Dog()
print(isinstance(d01, Dog))
print(isinstance(d01, Animal))

print(issubclass(Bird, Dog))

print(type(d01) == Animal)
