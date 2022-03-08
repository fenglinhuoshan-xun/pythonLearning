"""
    这个是skill_manager模块
"""
from skill_system.skill_deployer import SkillDeployer


class SkillManager:
    def generate(self):
        print("生成技能")


deployer = SkillDeployer()
deployer.deploy()
