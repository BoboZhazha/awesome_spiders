# -*- coding: utf-8 -*-
import scrapy


class ChangdeSpider(scrapy.Spider):
    name = 'changde'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
