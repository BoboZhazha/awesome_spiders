# -*- coding: utf-8 -*-

import scrapy
from government_spider.items import GovSpiderItem
import re


class LiaoNingSpider(scrapy.Spider):
    name = "liaoning"
    def start_requests(self):
        yield scrapy.Request('https://www.chinabidding.cn/sa/liaoning_gcjs/1.html')
        yield scrapy.Request('https://www.chinabidding.cn/sa/liaoning_zfgc/1.html')

    def parse(self, response):

        max_page_temp1 = response.xpath('//div[@id="pageZone"]/span/@title')
        if len(max_page_temp1) >4:
            max_page_temp = max_page_temp1[-2].extract()
            index = max_page_temp.find(u'页')
            max_page = max_page_temp[1:index]

        else:
            max_page = response.xpath('//div[@id="pageZone"]/span/text()').extract_first()

        contents = response.xpath('//div[@class="dq_nl"]/ul')[1:]
        for content in contents:
            title = content.xpath('.//li[@class="td_1"]/a/text()').extract_first()
            date = content.xpath('.//li[@class="td_2 dq_rq"]/text()').extract_first()
            short_url = content.xpath('.//li[@class="td_1"]/a/@href').extract_first()
            detail_url = "https://www.chinabidding.cn/"+short_url
            if "liaoning_gcjs" in response.url:
                content_type = "02"
            else:
                content_type = "01"
            yield GovSpiderItem(title=title,date=date, detail_url=detail_url,area_code="辽宁", content_type=content_type, publish_id= "181818", thing_id="42")


        for i in range(2, int(max_page)+1):
            next_url = re.sub(r'[1-9]\d*', str(i), response.url)
            yield scrapy.Request(next_url)





