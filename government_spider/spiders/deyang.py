# -*- coding: utf-8 -*-
import scrapy


class DeyangSpider(scrapy.Spider):
    name = 'deyang'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
