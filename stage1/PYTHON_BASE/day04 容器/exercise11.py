"""
    公司有以下员工：
    经理：曹操，刘备，孙权
    技术：曹操，刘备，张飞，关羽
    请计算：
        是经理也是技术的有谁？
        是经理，不是技术的有谁？
        是技术，不是经理的有谁？
        身兼一职的有谁？
        经理和技术总共有多少人？
"""
dict_persons = {
    "经理": {"曹操", "刘备", "孙权"},
    "技术": {"曹操", "刘备", "张飞", "关羽"}
}
print(dict_persons["经理"] & dict_persons["技术"])
print(dict_persons["经理"] - dict_persons["技术"])
print(dict_persons["技术"] - dict_persons["经理"])
print(dict_persons["经理"] ^ dict_persons["技术"])
print(len(dict_persons["经理"] | dict_persons["技术"]))
