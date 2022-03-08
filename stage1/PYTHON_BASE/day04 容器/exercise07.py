"""
    在控制台中循环录入学生信息（名称、性别、年龄、成绩），如果名称录入为空,则停止录入
    数据结构：
    [
        {"nane":"悟空","sex":"男","age":23,"score":100}
    ]
"""
list_persons = []
while True:
    name = input("请输入名称：")
    if name == "":
        break
    sex = input("请输入性别：")
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    dict_person = {"name": name, "sex": sex, "age": age, "score": score}
    list_persons.append(dict_person)
print(list_persons)

for item in list_persons:
    print("我叫%s性别是%s今年%d岁啦考了%d分" % (item["name"], item["sex"], item["age"], item["score"]))
