"""
demo02_numpy numpy演示
"""

import numpy as np


ary = np.array([1,2,3,4,5,6]) 
print(ary,type(ary)) 

print(ary * 2) # [ 2  4  6  8 10 12]
print(ary + ary) # [ 2  4  6  8 10 12]

print(ary > 2) # [False False  True  True  True  True]
# 数组与数组的运算，是对应位置元素相运算
print(ary * ary) # [ 1  4  9 16 25 36]

ary2 = np.array([1,2,3,4,5])
# 报错，两个数组，维度不一致
print(ary * ary2) # ValueError: operands could not be broadcast together with shapes (6,) (5,) 

