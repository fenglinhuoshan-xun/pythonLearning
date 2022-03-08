"""
    csv模块示例
"""
import csv

# with open('test.csv', 'w',encoding='GBK') as f: # 如果想在windows中打开不乱码，可以指定编码方式
with open('test.csv', 'w') as f:
    # 初始化一个csv文件的写入对象
    writer = csv.writer(f)
    writer.writerow(['月光宝盒', '周星驰', '1993-01-01'])
