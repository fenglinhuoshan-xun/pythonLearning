"""
    模块相关概念
"""
# __all__变量：定义可导出成员，仅对from xx import *语句有效
from my_project.skill_system import *  # 如果只导入包，则用不了包中的模块，需要去包的__init__.py文件中，自定义__all__变量

skill_manager.SkillManager()

# __doc__变量：文档字符串
print(skill_manager.__doc__)  # 返回模块当中的文档字符串
# __file__变量：模块对应的文件路径名
print(__file__)  # 当回当前文件的绝对路径
print(skill_manager.__file__)  # 谁去点，返回谁的真实绝对路径
# __name__变量：模块自身名字，可以判断是否为主模块，当前模块如果是主模块，则变量的结果就不是模块自身名字了，而是__main__
print(__name__)  # __main__
