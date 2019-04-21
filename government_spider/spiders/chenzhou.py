# -*- coding: utf-8 -*-
import scrapy


class ChenzhouSpider(scrapy.Spider):
    name = 'chenzhou'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
