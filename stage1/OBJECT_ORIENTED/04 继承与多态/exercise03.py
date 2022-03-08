"""
    手雷爆炸，伤害玩家（扣血，碎屏）和敌人（扣血，头顶爆字）
    变化点：鸭子，房子...
    写出体现三大特征的代码：
        封装：根据需求分解出手雷类、玩家类、手雷类
        继承：使用攻击目标隔离手雷与玩家和敌人
        多态：手雷调用攻击目标，在玩家和敌人对象中体现了不同效果
            玩家和敌人分别重写了攻击目标的受伤方法
"""


class Grenade:
    def explode(self, target):
        target.damage()


class AttackTarget:
    def damage(self):
        print("扣血")


# -----------------------------

class Player(AttackTarget):

    def damage(self):
        super().damage()
        print("碎屏")


class Enemy(AttackTarget):
    def damage(self):
        super().damage()
        print("头顶爆字")


g01 = Grenade()
p01 = Player()
e01 = Enemy()
g01.explode(e01)
