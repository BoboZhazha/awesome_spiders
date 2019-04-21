# -*- coding: utf-8 -*-
import scrapy


class YibinSpider(scrapy.Spider):
    name = 'yibin'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
