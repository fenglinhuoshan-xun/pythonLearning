"""
    创建敌人类，数据：姓名，血量(0--100)，攻击力(1--50)
"""


class Enemy:
    def __init__(self, name="", hp=0, atk=0):
        self.name = name
        self.hp = hp
        self.atk = atk

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise Exception("血量超过范围")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 1 <= value <= 50:
            self.__atk = value
        else:
            raise Exception("攻击力超过范围")


e01 = Enemy("灭霸", 99, 50)
print(e01.hp)
print(e01.atk)
