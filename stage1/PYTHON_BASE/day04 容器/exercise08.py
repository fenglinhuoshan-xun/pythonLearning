"""
    在控制台中循环录入多个人的多个喜好，如果名称录入为空，则停止录入
    最终打印所有信息
    数据结构：
    {
        "于谦":["抽烟","喝酒","烫头"]
    }
"""
dict_persons = {}
while True:
    name = input("请输入名称：")
    if name == "":
        break
    # list_persons_hobby = []
    dict_persons[name] = []
    while True:
        hobby = input("请输入喜好：")
        dict_persons[name].append(hobby)
        # list_persons_hobby.append(hobby)
        if hobby == "":
            break
    # dict_persons[name] = list_persons_hobby
print(dict_persons)

for k, v_list_hobby in dict_persons.items():
    print(k + "喜欢：")
    for item in v_list_hobby:
        print(item)
