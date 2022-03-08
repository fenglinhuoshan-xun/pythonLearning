"""
    使用selenium + Chrome来爬取当当网python图书数据
"""
from selenium import webdriver
import time
import random

options = webdriver.ChromeOptions()
options.add_argument('--headless')
# 1. 打开浏览器
driver = webdriver.Chrome(options=options)
# 2. 输入url地址
driver.get('https://search.dangdang.com/?key=python&page_index=2')


def get_one_page():
    """"抓取一页的数据"""
    # 3. dd_list: 匹配所有电影信息的dd节点对象列表
    # table_list: [<element table at xxx>,<>,...]
    table_list = driver.find_elements_by_xpath('//*[@id="component_59"]/li')
    # 4. for循环依次遍历，提取每个电影的信息
    for table in table_list:
        # print(table.text) # 先打印一下，看有没有规律。正常讲，就是可以继续用table节点对象来find_elements_by_xpath()来提取想要的数据，如果有规律，就很方便
        # print('*' * 50)
        info_list = table.text.split('\n')
        # print(len(info_list))
        # print(info_list)
        if len(info_list) == 10:
            item = {}
            item['name'] = info_list[0].split(' ')[0].strip()
            item['book_info'] = info_list[1].strip()
            item['price'] = info_list[2].strip()
            item['pricing'] = info_list[4].strip()
            item['discount'] = info_list[5].strip()
            item['e-books_price'] = info_list[6].split('：')[1].strip()
            item['commnts'] = info_list[7].strip()
            item['Press'] = info_list[8].strip()
            print(item)
        if len(info_list) == 9:
            item = {}
            item['name'] = info_list[0].split(' ')[0].strip()
            item['book_info'] = info_list[1].strip()
            item['price'] = info_list[2].strip()
            item['pricing'] = info_list[4].strip()
            item['discount'] = info_list[5].strip()
            item['commnts'] = info_list[6].strip()
            item['Press'] = info_list[7].strip()
            print(item)
        if len(info_list) == 8:
            item = {}
            item['name'] = info_list[0].split(' ')[0].strip()
            item['price'] = info_list[1].strip()
            item['pricing'] = info_list[3].strip()
            item['discount'] = info_list[4].strip()
            item['commnts'] = info_list[5].strip()
            item['Press'] = info_list[6].strip()
            print(item)
        if len(info_list) == 7:
            item = {}
            item['name'] = info_list[0].split(' ')[0].strip()
            item['price'] = info_list[1].strip()
            item['pricing'] = info_list[3].strip()
            item['commnts'] = info_list[4].strip()
            item['Press'] = info_list[5].strip()
            print(item)


while True:
    get_one_page()
    # result = driver.find_element_by_xpath('//*[@id="12810"]/div[5]/div[2]/div/ul/li[10]').get_attribute(
    #     'class') == 'next none'
    # if not result:
    #     driver.find_element_by_link_text('下一页').click()
    #     time.sleep(random.uniform(1, 2))

    # 1. 查找节点时，如果找不到会抛出异常
    try:
        driver.find_element_by_link_text('下一页').click()
        # 点击之后，需要给页面元素的加载预留时间
    except:
        driver.quit()
        break

# 分情况对比
# 10
# ['零基础学Python（全彩版） Python3全新升级！超20万读者认可的彩色书，从基本概念到完整项目开发，助您快速掌握Python编程。全程视频+完整源码+215道课后题+实物魔卡+海量资源',
#  'Python3全新升级！超20万读者认可的彩色书，从基本概念到完整项目开发，助您快速掌握Python编程。全程视频 完整源码 215道课后题 实物魔卡 海量资源', '¥69.50', '定价：', '¥79.80',
#  ' (8.71折)', '电子书：¥27.93', '11843条评论', '明日科技(Mingri Soft) /2021-04-01 /吉林大学出版社', '加入购物车购买电子书收藏']

# 9
# ['Python爬虫技术——深入理解原理、技术与开发 网红技术专家！JetBrains大中华区市场部经理赵磊作序！超过300个实战案例，10万行源代码，22个综合实战项目，海量学习资料！',
#  'JetBrains大中华区市场部经理赵磊作序！超过300个实战案例，10万行源代码，22个综合实战项目，海量学习资料，1000套中英文简历模板。全书内容涵盖： 李宁 私房菜谱 ? Python爬虫基础知识 ? Python网络库 ? Python解析库 ? Python数据存储 ? Python异步数据抓取 ? Python移动App数据抓取 ? Python可见即可爬 ? Python Scrapy实战 ? Python项目实战 李宁 实战项目 ? 抓取小说目录与正文 ? 抓取豆瓣网图书榜单 ? 抓取房屋租赁信息 ? 抓取豆瓣网音乐排行榜 ? 抓取百度网站图片搜索中的图片 ? 抓取QQ空间说说 ? 可视化爬虫抓取和分析当当网图书评论',
#  '¥66.70', '定价：', '¥89.00', ' (7.5折)', '2129条评论', '李宁 /2020-01-01 /清华大学出版社', '加入购物车收藏']

# 8
# ['用Python编程和实践！数学教科书', '¥83.90', '定价：', '¥89.80', ' (9.35折)', '164条评论', '[日] 我妻 幸长 著 /2021-06-01 /水利水电出版社', '加入购物车收藏']

# 7
# ['Python OpenCV 从入门到实践（全彩版）', '¥98.00', '定价：', '¥98.00', '226条评论', '明日科技 赵宁 赛奎春 /2021-05-01 /吉林大学出版社', '加入购物车收藏']
