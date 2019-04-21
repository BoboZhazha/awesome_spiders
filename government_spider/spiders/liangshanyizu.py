# -*- coding: utf-8 -*-
import scrapy


class LiangshanyizuSpider(scrapy.Spider):
    name = 'liangshanyizu'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
