# -*- coding: utf-8 -*-
import scrapy


class NeijiangSpider(scrapy.Spider):
    name = 'neijiang'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
