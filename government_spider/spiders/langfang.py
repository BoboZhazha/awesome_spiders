# -*- coding: utf-8 -*-
import scrapy


class LangfangSpider(scrapy.Spider):
    name = 'langfang'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
