"""
    古代的称一斤有16两，请在终端中获取两，计算是几斤零几辆
    输入：100
    输出：6斤零4两
"""

liang_weight = int(input("请输入总两："))
jin = liang_weight // 16
liang = liang_weight % 16
print(f"{jin}斤零{liang}两")