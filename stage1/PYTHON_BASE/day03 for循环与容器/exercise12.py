"""
    在控制台中循环录入同学们的身高，如果输入为空，则停止
    打印所有人的身高（一行一个）
    打印总数
    打印最高、最低、和平均的身高
    使用max    min    sum
"""
list_height = []
while True:
    str_height = input("请输入身高：")
    if str_height == "":
        break
    list_height.append(float(str_height))

for item in list_height:
    print(item)
print(len(list_height))
print(max(list_height))
print(min(list_height))
print(sum(list_height) / len(list_height))
