# 结构清晰，主题鲜明
dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []

def buying():
    """
            购买
    """
    print_commodity_info()
    dict_order = create_order()
    list_order.append(dict_order)
    print("添加到购物车。")


def create_order():
    """
        创建订单
    :return: 字典类型的订单对象
    """
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    dict_order = {"cid": cid, "count": count}
    return dict_order


def print_commodity_info():
    for key, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


def shopping():
    """
        购物
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buying()
        elif item == "2":
            settlement()


def settlement():
    """
        结算
    """
    total_price = calculate_total_price()
    print_order_info()
    paying(total_price)


def paying(total_price):
    """
        支付
    :param total_price:数值类型的总价
    """
    while True:
        money = float(input("总价%d元，请输入金额：" % total_price))
        if money >= total_price:
            print("购买成功，找回：%d元。" % (money - total_price))
            list_order.clear()
            break
        else:
            print("金额不足.")


def print_order_info():
    for order in list_order:
        dict_commodity = dict_commodity_info[order["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (dict_commodity["name"], dict_commodity["price"], order["count"]))


def calculate_total_price():
    """
        计算总价
    :return: 数值类型的总价格
    """
    total_price = 0
    for order in list_order:
        dict_commodity = dict_commodity_info[order["cid"]]
        total_price += dict_commodity["price"] * order["count"]
    return total_price


shopping()
