# -*- coding: utf-8 -*-
import scrapy


class ZhangjiajieSpider(scrapy.Spider):
    name = 'zhangjiajie'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
