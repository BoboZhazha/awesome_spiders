# -*- coding: utf-8 -*-
import scrapy


class XiangtanSpider(scrapy.Spider):
    name = 'xiangtan'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
