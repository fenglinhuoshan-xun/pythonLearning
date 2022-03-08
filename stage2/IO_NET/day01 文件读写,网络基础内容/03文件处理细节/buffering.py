"""
文件细节处理
"""

# f = open('file', 'wb',5) #缓冲区大小

# f=open('file','w',1) #行缓冲

f=open('file','w') #默认缓冲区

while True:
    data = input(">>")
    if not data:
        break
    # f.write(data.encode())
    # f.write(data+'\n') #行缓冲遇到换行
    f.write(data)
    f.flush() #刷新缓冲区

f.close()
