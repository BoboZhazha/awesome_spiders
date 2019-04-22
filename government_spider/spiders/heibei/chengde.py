# -*- coding: utf-8 -*-
import scrapy


class ChengdeSpider(scrapy.Spider):
    name = 'chengde'
    allowed_domains = ['chengde.com']
    start_urls = ['http://chengde.com/']

    def parse(self, response):
        pass
