# -*- coding: utf-8 -*-
import scrapy


class DingzhouSpider(scrapy.Spider):
    name = 'dingzhou'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
