# -*- coding: utf-8 -*-
import scrapy


class ZigongSpider(scrapy.Spider):
    name = 'zigong'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
