"""
    在控制台中获取一个季度，打印相应的月份
    输入与输出；
        春   1月2月３月
        夏   4月5月6月
        秋   7月8月9月
        冬   10月11月12月
"""
season = input("请输入季度：")
if season == "春":
    print("1月2月3月")
elif season == "夏":
    print("4月5月6月")
elif season == "秋":
    print("7月8月9月")
else:
    print("10月11月12月")
