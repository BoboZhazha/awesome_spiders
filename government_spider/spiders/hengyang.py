# -*- coding: utf-8 -*-
import scrapy


class HengyangSpider(scrapy.Spider):
    name = 'hengyang'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
