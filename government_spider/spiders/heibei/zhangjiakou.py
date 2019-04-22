# -*- coding: utf-8 -*-
import scrapy


class ZhangjiakouSpider(scrapy.Spider):
    name = 'zhangjiakou'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
