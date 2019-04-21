# -*- coding: utf-8 -*-
import scrapy


class ShijiazhuanSpider(scrapy.Spider):
    name = 'shijiazhuan'
    allowed_domains = ['shijiazhuang.com']
    start_urls = ['http://shijiazhuang.com/']

    def parse(self, response):
        pass
