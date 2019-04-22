# -*- coding: utf-8 -*-
import scrapy


class CangzhouSpider(scrapy.Spider):
    name = 'cangzhou'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
