"""
    包
    导入是否成功的条件：
    系统路径 + 导入路径 == 真实路径
"""
# 导入方式1：import 路径.模块名 as 别名
# 使用：别名.成员
import package01.m01 as m

m.func01()

# 导入方式2：from 路径.模块名 import 成员
# 使用：直接使用成员
from package01.package02.m02 import func02

func02()

# 导入方式3：from 路径.模块名 import *
# 使用：直接使用成员
from package01.package02.m02 import *

func02()
