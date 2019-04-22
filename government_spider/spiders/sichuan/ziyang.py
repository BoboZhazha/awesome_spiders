# -*- coding: utf-8 -*-
import scrapy


class ZiyangSpider(scrapy.Spider):
    name = 'ziyang'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
