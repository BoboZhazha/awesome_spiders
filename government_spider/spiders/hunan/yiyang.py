# -*- coding: utf-8 -*-
import scrapy


class YiyangSpider(scrapy.Spider):
    name = 'yiyang'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
