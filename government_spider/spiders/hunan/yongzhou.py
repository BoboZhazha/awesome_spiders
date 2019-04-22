# -*- coding: utf-8 -*-
import scrapy


class YongzhouSpider(scrapy.Spider):
    name = 'yongzhou'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
