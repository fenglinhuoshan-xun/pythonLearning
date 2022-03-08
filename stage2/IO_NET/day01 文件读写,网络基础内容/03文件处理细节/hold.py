f=open('file','wb+')

f.write(b'a')
f.seek(1024)
f.write(b'b')
f.seek(-1,2)
data=f.read()
print(data)

f.close()