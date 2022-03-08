"""
文件写操作
"""

f=open('file', 'w')
#
# n=f.write(b"Python\n")
# print("写入了%d个字符" % n)
# n=f.write(b"Python\n")
# print("写入了%d个字符" % n)

list=['hello\n','world']
f.writelines(list)

f.close()