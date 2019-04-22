# -*- coding: utf-8 -*-
import scrapy


class BazhongSpider(scrapy.Spider):
    name = 'bazhong'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
