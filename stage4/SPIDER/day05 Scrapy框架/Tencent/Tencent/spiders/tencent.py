# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
import scrapy
import json
from ..items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']

    def start_requests(self):
        """一次性生成所有要抓取的url地址，一次性交给调度器入队列"""
        job_kw = quote(input('请输入职位名称：'))
        for i in range(1, 6):
            url = 'https://careers.tencent.com/tencentcareer/api/post/Query?keyword={}&pageIndex={}&pageSize=10'.format(
                job_kw, i)
            yield scrapy.Request(url=url, callback=self.detail_page)

    def detail_page(self, response):
        data = json.loads(response.body)["Data"]
        list_objs = data["Posts"]
        for job in list_objs:
            item = TencentItem()
            item['job_name'] = job["RecruitPostName"].strip()
            item['job_addr'] = job["LocationName"].strip()
            item['update_time'] = job["LastUpdateTime"].strip()

            # 把招聘详情页的链接交给调度器入队列，一定是等所有的数据都提完后，再交给调度器入队列
            # meta参数：在不同的解析函数之间传递数据，将这个对象传递下去
            two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId={}'.format(job['PostId'])
            yield scrapy.Request(url=two_url, meta={'item': item}, callback=self.get_career_info)

    def get_career_info(self, response):
        job_data = json.loads(response.body)["Data"]
        # meta会随着response一起回来，作为response的一个属性
        item = response.meta['item']
        item['responsibility'] = job_data["Responsibility"].replace('\xa0', '').replace('\n', '')
        item['requirement'] = job_data["Requirement"].replace('\xa0', '').replace('\n', '')

        # 至此，一个职位的完整信息提取完成！交给管道文件去处理
        yield item
