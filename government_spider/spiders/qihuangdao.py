# -*- coding: utf-8 -*-
import scrapy


class QihuangdaoSpider(scrapy.Spider):
    name = 'qihuangdao'
    allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']

    def parse(self, response):
        pass
