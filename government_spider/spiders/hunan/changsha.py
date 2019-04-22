# -*- coding: utf-8 -*-
import scrapy


class ChangshanSpider(scrapy.Spider):
    name = 'changsha'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
