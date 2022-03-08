import sys

sys.path.append("/home/xiaoshoubingliang/PycharmProjects/stage1/PYTHON_ADVANCED/my_project")
print(sys.path)
from common.list_helper import ListHelper


class SkillDeployer:
    def deploy(self):
        print("释放技能")


ListHelper.get_elements()
