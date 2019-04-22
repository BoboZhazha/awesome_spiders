# -*- coding: utf-8 -*-
import scrapy


class MianyangSpider(scrapy.Spider):
    name = 'mianyang'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
