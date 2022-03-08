"""
    闭包应用
        1. 逻辑连续 在python中，针对逻辑连续的问题，通常是用面向对象解决的。因为有的语言没有面向对象，所以想解决逻辑连续的问题，只能用闭包
        2. 装饰器
"""


def give_gife_money(money):
    print("得到了", money, "元压岁钱")

    def child_buy(target, price):
        nonlocal money
        money -= price
        print("购买了", target, "还剩", money, "元")

    return child_buy


action = give_gife_money(500)
action("变形金刚", 130)
action("遥控飞机", 250)
action("零食", 120)
