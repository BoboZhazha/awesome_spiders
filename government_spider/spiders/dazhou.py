# -*- coding: utf-8 -*-
import scrapy


class DazhouSpider(scrapy.Spider):
    name = 'dazhou'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
