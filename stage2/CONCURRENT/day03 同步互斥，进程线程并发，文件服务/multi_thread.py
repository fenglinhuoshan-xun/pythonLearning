from test import *
from threading import Thread
import time

jobs = []

tm = time.time()

for i in range(10):
    # t = Thread(target=count, args=(1, 1))  # Thread cpu: 6.667380094528198
    t = Thread(target=io)  # Thread io: 5.820189952850342
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()

print("Thread cpu:", time.time() - tm)
