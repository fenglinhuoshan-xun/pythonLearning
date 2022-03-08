f = open('file', 'wb+')

f.write(b"hello world")

print("文件偏移量", f.tell())

f.seek(-5, 2)  #将文件偏移量设置到开头

data = f.read()
print(data)

f.close()
