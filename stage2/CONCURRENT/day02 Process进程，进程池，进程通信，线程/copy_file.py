"""
创建两个进程
分别复制文件的上半部分和下半部分到一个新的文件中
"""

from multiprocessing import Process
import os

filename = './1.jpg'
size = os.path.getsize(filename)


# 父进程创建fr 两个子进程使用这个fr会相互影响
# 我们的IO在操作系统层面上有一个维护，如果在父进程中打开，在子进程中是使用的，但两个子进程会相互影响，因为操作系统会认为是同一个IO操作，文件偏移量会互相影响
# fr = open(filename,'rb')

# 复制上半部分
def top():
    fr = open(filename, 'rb')
    fw = open('top.jpg', 'wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()


# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open('bot.jpg', 'wb')
    fr.seek(size // 2, 0)
    fw.write(fr.read())
    fr.close()
    fw.close()


p1 = Process(target=top)
p2 = Process(target=bot)
p2.start()
p1.start()
p1.join()
p2.join()
