"""
在控制台中录入商品信息（名称和单价）
如果名称录入为空，则停止录入
最后打印所有商品信息（一行一个）
如果录入了游戏机，则打印其价格
"""
dict_commodity = {}
while True:
    name = input("请商品的名称：")
    if name == "":
        break
    price = int(input("请输入单价："))
    dict_commodity[name] = price
for k,v in dict_commodity.items():
    print("%s商品的价格是%d" % (k,v))
if "游戏机" in dict_commodity:
    print(dict_commodity["游戏机"])