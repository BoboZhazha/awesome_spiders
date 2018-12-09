# -*- coding: utf-8 -*-

from government_spider.items import GovernmentSpiderItem
import scrapy
import re

class HunanSpider(scrapy.Spider):
    name = "hunan"
    def start_requests(self):
        yield scrapy.Request('http://www.hngzzx.com/jydt/002002/002002001/002002001001/1.html')
        yield scrapy.Request('http://www.hngzzx.com/jydt/002002/002002002/002002002001/1.html')
        yield scrapy.Request('http://www.hngzzx.com/jydt/002002/002002003/002002003001/1.html')
        yield scrapy.Request('http://www.hngzzx.com/jydt/002002/002002006/002002006001/1.html')

    def parse(self, response):
        max_page_temp = response.xpath('//div[@class="ewb-page"]//li[@class="ewb-page-li ewb-page-noborder ewb-page-num"]/span/text()').extract_first()
        max_page = max_page_temp.split('/')[1]
        contents = response.xpath('//ul[@class="wb-data-item"]/li')
        for content in contents:
            title = content.xpath('.//div[@class="wb-data-infor l"]/a/text()').extract_first()
            date = content.xpath('.//span[@class="wb-data-date"]/text()').extract_first()
            short_url = content.xpath('.//div[@class="wb-data-infor l"]/a/@href').extract_first()
            detail_url = "http://www.hngzzx.com"+short_url
            if "002002001001" in response.url:
                content_type = "02"
            elif "002002002001" in response.url:
                content_type = "01"
            elif "002002003001" in response.url:
                content_type = "03"
            else:
                content_type = "04"
            yield GovernmentSpiderItem(title=title,date=date, detail_url=detail_url,area_code="HUNAN", content_type=content_type, publish_id= "181818", thing_id="42")
        for page in range(2, int(max_page)+1):
            next_url = re.sub(r"[1-9]\d*.html", str(page)+".html", response.url)
            yield scrapy.Request(url=next_url)

