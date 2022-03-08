"""
僵尸进程
"""
import os
import signal

# 信号方法处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child Process:", os.getpid())  # 去终端中ps -aux，看一下此时僵尸进程存在于系统中
    os._exit(1)
else:
    # p, status = os.wait()
    # print("PID:", p)
    # print("Status:", status) # 256
    # print("Status:", os.WEXITSTATUS(status))  # 1

    while True:
        pass
