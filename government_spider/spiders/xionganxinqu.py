# -*- coding: utf-8 -*-
import scrapy


class XionganxinquSpider(scrapy.Spider):
    name = 'xionganxinqu'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
