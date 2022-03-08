"""
文件读取演示
"""
f = open('file')

# 文件读操作
# data = f.read(1024)
# print(data)
#
# f.close()

# 通过循环读取
# while True:
#     data=f.read(2)
#     if not data:
#         break
#     print(data)
# data = f.readline()
# print(data)
# data=f.readline(14)
# print(data)
# data=f.readline(4)
# print(data)
# while True:
#     data=f.readline()
#     if not data:
#         break
#     print(data)
# data=f.readlines(12)
# print(data)
for line in f:
    print(line)

f.close()
