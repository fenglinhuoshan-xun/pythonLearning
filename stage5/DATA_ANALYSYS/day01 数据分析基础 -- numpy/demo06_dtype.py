"""
demo06_dtype.py 复合数据类型
"""
import numpy as np

data = [('zs', [90, 98, 96], 15),
        ('ls', [91, 92, 92], 16),
        ('ww', [92, 95, 94], 17)]

ary = np.array(data, dtype='2str,3int32,int32')
# [('zs', [90, 98, 96], 15) ('ls', [91, 92, 92], 16)
#  ('ww', [92, 95, 94], 17)] 17
print(ary,ary[2][2])

# names里面我们可以为每个字段定义一个别名，formats里可以指定每个字段的数据类型
# 有了别名之后，我们之后访问就可以通过别名来访问字段了，而不用通过下标来访问
ary = np.array(data,dtype={'names':['name','score','age'],'formats':['2str','3int32','int32']})
# [('zs', [90, 98, 96], 15) ('ls', [91, 92, 92], 16)
#  ('ww', [92, 95, 94], 17)] 17
print(ary,ary[2]['age'])

# 在列表当中，用每一个元祖去定义每一个字段的数据类型
ary = np.array()

