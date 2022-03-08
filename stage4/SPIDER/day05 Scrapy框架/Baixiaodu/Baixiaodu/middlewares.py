# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class BaixiaoduSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BaixiaoduDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 中间件1 -- 随机User-Agent
from fake_useragent import UserAgent


class BaixiaoduRandomDownloaderMiddleware(object):
    def process_request(self, request, spider):
        agent = UserAgent().random
        # Request()方法中所有的参数都可以作为请求对象request的属性
        # Request()方法中的参数有啥？url meta callback headers cookies
        request.headers['User-Agent'] = agent
        print(agent)


# 中间件2 -- 随机代理
import random
from .proxies import proxy_list


class BaixiaoduRandomProxyDownloaderMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(proxy_list)
        # 如何赋值给请求对象？使用某个属性，meta属性
        # meta：既可以在不同解析函数之间传递数据，又可以定义代理
        request.meta['proxy'] = proxy  # 键是定死的
        print(proxy)

    def process_exception(self, request, exception, spider):
        """因为代理IP可能不能使用，scrapy会自动尝试3次后抛出异常，我们当然想让它一直尝试"""
        return request


# 中间件3 -- Cookie
class BaixiaoduCookieDownloaderMiddleware(object):
    def process_request(self, request, spider):
        cookie_dict = self.get_cookies()
        # 用什么属性添加cookie的中间件？答案是：cookies属性
        request.cookies = cookie_dict
        print(cookie_dict)

    def get_cookies(self):
        cookie_string = 'BIDUPSID=FBFD588A96601EAF76BA0702C2780DF2; PSTM=1611231749; BAIDUID=FBFD588A96601EAF319299917E11680C:FG=1; __yjs_duid=1_b2c7b897f756f6699fab40e799e00eec1619517378660; BDUSS=TBUci1lS1VSdWlJZkRlajlObzdMaTBqZEcwUC1ERzA1RGYtOXRFSWVRWElZOHRnRVFBQUFBJCQAAAAAAAAAAAEAAACzA1fH1sHX8NDH0qvRsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjWo2DI1qNgT; BDUSS_BFESS=TBUci1lS1VSdWlJZkRlajlObzdMaTBqZEcwUC1ERzA1RGYtOXRFSWVRWElZOHRnRVFBQUFBJCQAAAAAAAAAAAEAAACzA1fH1sHX8NDH0qvRsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjWo2DI1qNgT; BD_UPN=12314753; ispeed_lsm=0; BAIDUID_BFESS=9F8782763FFF76F8002D873EFB492BE2:FG=1; __sec_t_key=d060de42-716d-4ace-9653-735c15805b0d; baikeVisitId=62024c37-0559-459e-8c5b-00839c041f28; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=7; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1637585369,1638285174,1638327890; Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1638327890; COOKIE_SESSION=43058_1_9_9_16_15_1_0_7_4_212_2_39967_0_10_0_1638327896_1638183124_1638327886%7C9%23598390_47_1638183123%7C9; H_PS_PSSID=35359_35104_31660_35239_34584_34517_35233_34606_35316_26350_35115_22159; BA_HECTOR=0l8k8l85042lak81mo1gqf5em0r'
        cookie_dict = {}
        for kv in cookie_string.split('; '):
            # kv: BIDUPSID=FBFD588A96601EAF76BA0702C2780DF2 ...
            k = kv.split('=')[0]
            v = kv.split('=')[1]
            cookie_dict[k] = v

        return cookie_dict
