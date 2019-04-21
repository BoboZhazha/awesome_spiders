# -*- coding: utf-8 -*-
import scrapy


class ChengduSpider(scrapy.Spider):
    name = 'chengdu'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
