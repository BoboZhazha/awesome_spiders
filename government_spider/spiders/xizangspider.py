# -*-coding:utf-8 -*-

import scrapy
import re
from government_spider.items import GovSpiderItem
import time


class XiZangSpider(scrapy.Spider):
    # 完成
    name = "xizang"

    def start_requests(self):
        yield scrapy.Request('http://www.xzggzy.gov.cn:9090/zbzsgg/index_1.jhtml')
        yield scrapy.Request('http://www.xzggzy.gov.cn:9090/td/index_1.jhtml')
        yield scrapy.Request('http://www.xzggzy.gov.cn:9090/cggg/index_1.jhtml')

    def parse(self, response):
        max_page_temp = response.xpath('//div[@class="pages"]/ul[@class="pages-list"]/li[1]/a/text()').extract_first()
        max_page1 = max_page_temp.split('/')[1]
        index = max_page1.find(u'页')
        max_page = max_page1[:index]

        contents = response.xpath('//ul[@class="article-list-old"]/li')
        for content in contents:
            title = content.xpath('.//a/@title').extract_first()
            date1 = content.xpath('.//div[@class="list-times-old"]/text()').extract_first()
            date2 = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
            date = time.strftime("%Y-%m-%d", date2)
            detail_url = content.xpath('.//a/@href').extract_first()
            if "zbzsgg" in response.url:
                content_type = "02"
            elif "td" in response.url:
                content_type = "03"
            else:
                content_type = "04"
            yield GovSpiderItem(notice_title=title,notice_date=date, detail_url=detail_url,area_code="西藏", content_type=content_type, publish_id= "540000", thing_type_id="88")

        for i in range(2, int(max_page)+1):
            next_url = re.sub(r'index_[1-9]\d*', "index_"+str(i), response.url)
            yield scrapy.Request(next_url)
