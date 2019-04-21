# -*- coding: utf-8 -*-
import scrapy


class BaodingSpider(scrapy.Spider):
    name = 'baoding'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
