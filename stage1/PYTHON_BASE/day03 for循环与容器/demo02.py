"""
    循环计数
"""
# range(开始值，结束值，间隔)  不能包含结束值
for item in range(1,10,1):
    print(item)

# range(结束值)  开始值默认为0，间隔默认为1
for item in range(10):
    print(item)

for item in range(3,10,2):
    print(item)

for item in range(8,1,-1):
    print(item)