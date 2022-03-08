from scrapy import cmdline

cmdline.execute('scrapy crawl baidu'.split())  # 不加split()，会以为这个字符串是一个参数，加了之后，会以为是三个


