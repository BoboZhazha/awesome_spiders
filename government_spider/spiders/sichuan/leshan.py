# -*- coding: utf-8 -*-
import scrapy


class LeshanSpider(scrapy.Spider):
    name = 'leshan'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
