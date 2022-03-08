"""
    创建列表，存储水星，金星，地球，木星，土星，天王星
    向列表中追加海王星
    在地球后追加火星
    打印距离太阳最远的行星（最后一个行星）
    打印地球之前的所有行星（前两个行星）
    删除金星
    删除地球后面的所有行星
    倒序打印所有行星
"""
list_planet = ["水星", "金星", "地球", "木星", "土星", "天王星"]
list_planet.append("海王星")
list_planet.insert(3, "火星")
print(list_planet[-1])
print(list_planet[:2])
list_planet.remove("金星")
del list_planet[3:]
for item in range(len(list_planet) - 1, -1, -1):
    print(list_planet[item])
