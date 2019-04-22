# -*- coding: utf-8 -*-
import scrapy


class TangshanSpider(scrapy.Spider):
    name = 'tangshan'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
