# -*- coding: utf-8 -*-
import scrapy


class PanzhihuaSpider(scrapy.Spider):
    name = 'panzhihua'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
