"""
    在控制台中输出：0 1 2 3 4 5
    在控制台中输出：2 3 4 5 6 7
    在控制台中输出：0 2 4 6
    在控制台中输出：4 3 2 1 0
    在控制台中输出：-1 -2 -3 -4
"""
count = 0
while count <= 5:
    print(count)
    count += 1

count = 2
while count <= 7:
    print(count)
    count += 1

count = 0
while count <= 6:
    print(count)
    count += 2

count = 4
while count >= 0:
    print(count)
    count -= 1

count = -1
while count >= -4:
    print(count)
    count -= 1

# count = -1
# while count < 5:
#     count += 1
#     print(count)

# count = 1
# while count < 7:
#     count += 1
#     print(count)
#
# count = -2
# while count < 6:
#     count += 2
#     print(count)

# count = 5
# while count > 0:
#     count -= 1
#     print(count)

# count = 0
# while count > -4:
#     count -= 1
#     print(count)
