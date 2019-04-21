# -*- coding: utf-8 -*-
import scrapy


class HengshuiSpider(scrapy.Spider):
    name = 'hengshui'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
