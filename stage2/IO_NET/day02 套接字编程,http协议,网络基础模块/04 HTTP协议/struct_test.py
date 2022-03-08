"""
数据打包
"""
import struct

# 1 lily 18 1.65
fmt = "i4sif"

# st = struct.Struct(fmt)
#
# data = st.pack(1,b'Tom',18,1.65)
# print(data)
#
# data = st.unpack(data)
# print(data)

# pack和unpack的另一种用法，只需要将设置的格式作为第一个参数写在pack和unpack函数的参数中即可
# 不过还是要注意，打包和解包的格式要一致
data = struct.pack(fmt,1,b'lucy',18,1.66)
print(data)

data = struct.unpack(fmt,data)
print(data)