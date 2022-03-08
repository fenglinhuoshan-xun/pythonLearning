"""
demo05_dtype.py 基本数据类型
"""
import numpy as np

ary = np.array([1, 2, 3, 4])
print(ary, ary.dtype)  # [1 2 3 4] int64

ary = np.array([1, 2, 3, 4],dtype='int32')
print(ary, ary.dtype)  # [1 2 3 4] int32

ary = np.array([1, 2, 3, 4],dtype='float32')
print(ary, ary.dtype)  # [1 2 3 4] float32

ary = ary.astype('float64')
print(ary,ary.dtype) # [1. 2. 3. 4.] float64

# ary = ary.astype('bool')
# print(ary,ary.dtype) # [ True  True  True  True] bool

ary = ary.astype('str')
print(ary,ary.dtype) # ['1.0' '2.0' '3.0' '4.0'] <U32
