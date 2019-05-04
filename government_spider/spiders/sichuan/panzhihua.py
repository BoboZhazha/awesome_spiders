# -*- coding: utf-8 -*-
import scrapy
# 攀枝花
class PanzhihuaSpider(scrapy.Spider):
    name = 'panzhihua'
    start_urls = ['http://www.pzhggzy.cn/jyxx/jsgcZbgg']


    # 这个网站先拿左边的数据分类, 然后每页都找到最大页码,然后开始
    def start_requests(self):

        yield scrapy.Request(
            url='http://www.pzhggzy.cn/jyxx/jsgcZbgg')

    def parse(self, response):
        response.xpath()

        pass
