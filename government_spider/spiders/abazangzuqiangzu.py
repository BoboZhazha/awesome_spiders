# -*- coding: utf-8 -*-
import scrapy


class AbazangzuqiangzuSpider(scrapy.Spider):
    name = 'abazangzuqiangzu'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
