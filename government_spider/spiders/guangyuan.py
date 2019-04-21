# -*- coding: utf-8 -*-
import scrapy


class GuangyuanSpider(scrapy.Spider):
    name = 'guangyuan'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
