# -*- coding: utf-8 -*-
import scrapy


class MeishanSpider(scrapy.Spider):
    name = 'meishan'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
