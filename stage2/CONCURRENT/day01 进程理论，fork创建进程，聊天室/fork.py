import os

print("=================")  # 只执行了一次，父进程中执行了，子进程中没执行
a = 1
pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:  # 子进程执行部分
    print("The new process")
    print('a =', a)  # 子进程不会执行fork之前的代码，但是能获取相应的内存空间，此时操作的是自己的a了
else:  # 父进程执行部分
    print("The old process")

print("fork test over")
print("all a = ", a)  # 此时应该打印两次
