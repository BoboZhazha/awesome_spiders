# -*- coding: utf-8 -*-
import scrapy


class LuzhouSpider(scrapy.Spider):
    name = 'luzhou'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
