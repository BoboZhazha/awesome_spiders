# -*- coding: utf-8 -*-
import scrapy


class SuiningSpider(scrapy.Spider):
    name = 'suining'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
