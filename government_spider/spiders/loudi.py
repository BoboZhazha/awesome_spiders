# -*- coding: utf-8 -*-
import scrapy


class LoudiSpider(scrapy.Spider):
    name = 'loudi'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
