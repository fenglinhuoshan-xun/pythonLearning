from test import *
from multiprocessing import Process
import time

jobs = []

tm = time.time()
for i in range(10):
    # p = Process(target=count, args=(1, 1))  # Process cpu: 4.010796308517456
    p = Process(target=io)  # Process io: 2.524371862411499
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print("Process cpu:", time.time() - tm)
