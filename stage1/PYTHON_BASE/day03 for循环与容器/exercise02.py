"""
循环累加下列数字的和：0 1 2 3 4 5
循环累加下列数字的和：2 3 4 5 6 7
循环累加下列数字的和：0 2 4 6
循环累加下列数字的和：4 3 2 1 0
循环累加下列数字的和：-1 -2 -3 -4
"""
sum_value = 0
for i in range(6):
    sum_value += i
print(sum_value)

sum_value = 0
for i in range(2,8):
    sum_value += i
print(sum_value)

sum_value = 0
for i in range(0,7,2):
    sum_value += i
print(sum_value)

sum_value = 0
for i in range(4,-1,-1):
    sum_value += i
print(sum_value)

sum_value = 0
for i in range(-1,-5,-1):
    sum_value += i
print(sum_value)