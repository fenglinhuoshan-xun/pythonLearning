"""
demo03_ndarray.py numpy演示
"""
import numpy as np


ary = np.array([[1, 3, 5], [2, 4, 6]])
# [[1 3 5]
#  [2 4 6]]
print(ary)

ary2 = np.arange(0, 10, 2)  # [0 2 4 6 8]
print(ary2)

# 注意，里面每个元素默认都是浮点类型，我们可以修改数组里元素的数据类型
ary3 = np.ones(10)  # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
print(ary3)

ary3 = np.zeros(10, dtype='float32')  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
print(ary3)

ary3 = np.zeros(10, dtype='int32')  # [0 0 0 0 0 0 0 0 0 0]
print(ary3)

ary4 = np.ones_like(ary)
# [[1 1 1]
#  [1 1 1]]
print(ary4)

ary5 = np.zeros_like(ary)
# [[0 0 0]
#  [0 0 0]]
print(ary5)

print(np.ones(5) / 5) # [0.2 0.2 0.2 0.2 0.2]
