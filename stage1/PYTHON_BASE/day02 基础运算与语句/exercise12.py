"""
    使下列代码循环执行，直到录入"exit"退出程序
    season = input("请输入季度：")
    if season == "春":
        print("1月2月3月")
    elif season == "夏":
        print("4月5月6月")
    elif season == "秋":
        print("7月8月9月")
    else:
        print("10月11月12月")
"""
while True:
    season = input("请输入季度：")
    if season == "春":
        print("1月2月3月")
    elif season == "夏":
        print("4月5月6月")
    elif season == "秋":
        print("7月8月9月")
    else:
        print("10月11月12月")
    if input("请输入exit退出：") == "exit":
        break
