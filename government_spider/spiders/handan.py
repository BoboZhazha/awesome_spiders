# -*- coding: utf-8 -*-
import scrapy


class HandanSpider(scrapy.Spider):
    name = 'handan'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
