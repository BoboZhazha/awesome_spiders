# -*- coding: utf-8 -*-
import scrapy


class YueyangSpider(scrapy.Spider):
    name = 'yueyang'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
