"""
    技能系统
"""


class ImpactEffect:
    """
        影响效果
    """

    def impact(self):
        pass


class DamageEffect(ImpactEffect):
    def __init__(self, value=0):
        self.value = value

    def impact(self):
        super().impact()
        print("伤害%d生命" % self.value)


class CostSPEffect(ImpactEffect):
    def __init__(self, value=0):
        self.value = value

    def impact(self):
        super().impact()
        print("消耗%d法力" % self.value)


class LowerDeffenseEffect(ImpactEffect):
    def __init__(self, value=0, time=0):
        self.value = value
        self.time = time

    def impact(self):
        super().impact()
        print("降低%.1f防御力，持续%.1f时间" % (self.value, self.time))


class SkillBaseData:
    def __init__(self, name="", level=0):
        self.name = name
        self.level = level


class SkillDeployer:
    """
        技能释放器
    """

    def __init__(self, base_data=None):
        self.base_data = base_data
        self.__config_file = self.__load_congig_file()
        self.__effect_object = self.__create_effect_object()

    def __load_congig_file(self):
        return {
            "降龙十八掌": ["DamageEffect(260)", "CostSPEffect(100)"],
            "六脉神剑": ["DamageEffect(100)", "LowerDeffenseEffect(0.7,5)"]
        }

    def __create_effect_object(self):
        # 根据当前技能名称，获取影响效果名称
        effect_names = self.__config_file[self.base_data.name]
        # effect_object = []
        # for item in effect_names:
        #     obj = eval(item)
        #     effect_object.append(obj)
        #     return effect_object
        return [eval(item) for item in effect_names]

    def generate_skill(self):
        for item in self.__effect_object:
            item.impact()


# 测试
xlsbz = SkillDeployer(SkillBaseData("降龙十八掌", 1))
xlsbz.generate_skill()

lmsj = SkillDeployer(SkillBaseData("六脉神剑", 1))
lmsj.generate_skill()
