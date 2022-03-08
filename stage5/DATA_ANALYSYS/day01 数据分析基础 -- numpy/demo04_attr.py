"""
demo04_attr.py 属性基本操作
"""
import numpy as np

ary = np.arange(1, 10)
print(ary)  # [1 2 3 4 5 6 7 8 9]

# shape属性
print(ary, ary.shape)  # [1 2 3 4 5 6 7 8 9] (9,)

# 可以直接改变属性
ary.shape = (3, 3)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]] (3, 3)
print(ary, ary.shape)

# dtype属性
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]] int64
# 不同的操作系统，可能这个地方不一样，因为numpy因为操作系统的原因，导致默认的数据类型不一致，这个无所谓
print(ary, ary.dtype)

# ry.dtype = 'float32'
# [[1.4e-45 0.0e+00 2.8e-45 0.0e+00 4.2e-45 0.0e+00]
#  [5.6e-45 0.0e+00 7.0e-45 0.0e+00 8.4e-45 0.0e+00]
#  [9.8e-45 0.0e+00 1.1e-44 0.0e+00 1.3e-44 0.0e+00]] float32
# 这种做法强制把int64转为float32，然后按照float的方式去解析，是不可取的
# print(ary,ary.dtype)

# 我们一般转数据类型，是利用astype方法，参数为目标数据类型
ary = ary.astype('float32')
# [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]] float32
print(ary, ary.dtype)

# size属性
# ary.size：表示ndarray数组中有多少个最小单元，即有多少个元素
# len(ary)：表示ndarray数组里，小一级的数组里有多少个元素
print(ary.size, len(ary))  # 9 3
print(len([1, 1, 1]))  # 3


