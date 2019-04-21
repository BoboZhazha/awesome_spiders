# -*- coding: utf-8 -*-
import scrapy


class ZhuzhouSpider(scrapy.Spider):
    name = 'zhuzhou'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
