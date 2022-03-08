"""
处理二级界面
"""


def fun():
    while True:
        print("二级界面")
        cmd = input(">>")
        if cmd == 'a':
            print('a')
        elif cmd == 'b':
            print('b')
        elif cmd == 'c':
            break


while True:
    print("一级界面")
    cmd = input(">>")
    if cmd == '1':
        print(1)
    elif cmd == '2':
        fun()
    elif cmd == '3':
        fun()
