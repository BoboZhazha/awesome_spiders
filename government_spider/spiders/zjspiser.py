# -*-coding:utf-8 -*-

import scrapy
import logging
from government_spider.items import GovSpiderItem
import scrapy
class ZhejiangSpider(scrapy.Spider):
    # 浙江的问题是入库以后发现有大量重复数据 日期和title稍微做下处理
    name = 'zhejiang'
    # allowed_domains = ['zhejiang.com']
    #start_urls = ['http://new.zmctc.com/zjgcjy/jyxx/004001/004001001/',
                  #'http://new.zmctc.com/zjgcjy/jyxx/004001/004001002/',
                  #'http://new.zmctc.com/zjgcjy/jyxx/004001/004001003/',
                  #]
    def start_requests(self):
        yield scrapy.Request(url='http://new.zmctc.com/zjgcjy/jyxx/004001/004001001/')
        yield scrapy.Request(url='http://new.zmctc.com/zjgcjy/jyxx/004001/004001002/')
        yield scrapy.Request(url='http://new.zmctc.com/zjgcjy/jyxx/004001/004001003/')

    def parse(self, response):
        max_page_temp = response.xpath('//div[@class="pagemargin"]//td[@class="huifont"]/text()').extract_first()
        max_page = max_page_temp.split('/')[1]
        trs = response.xpath('//table[@width="98%"]/tr[@height="30"]')
        for tr in trs:
            title = tr.xpath('.//td[2]/a/@title').extract_first()
            date = tr.xpath('.//td[3]/text()').extract_first()[1:-1]
            short_url = tr.xpath('.//td[2]/a/@href').extract_first()
            detail_url = response.urljoin(short_url)
            if "004001001" in response.url:
                # 工程03
                content_type = "03"
            elif "004001002" in response.url:
                content_type = "01"
            else:
                content_type = "04"
            yield GovSpiderItem(title=title,date=date, detail_url=detail_url,area_code="ZHEJIANG", content_type=content_type, publish_id= "181818", thing_id="42")

        for page in range(2, int(max_page)+1):
            next_url = response.urljoin('?Page='+str(page))
            yield scrapy.Request(url=next_url)

