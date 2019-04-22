# -*- coding: utf-8 -*-
import scrapy


class YaanSpider(scrapy.Spider):
    name = 'yaan'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
