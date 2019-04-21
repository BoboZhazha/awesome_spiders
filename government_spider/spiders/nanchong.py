# -*- coding: utf-8 -*-
import scrapy


class NanchongSpider(scrapy.Spider):
    name = 'nanchong'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
