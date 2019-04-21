# -*- coding: utf-8 -*-
import scrapy


class GanzizangzuSpider(scrapy.Spider):
    name = 'ganzizangzu'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
