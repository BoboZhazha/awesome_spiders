# -*- coding:utf-8 -*-
import scrapy
from government_spider.items import GovernmentSpiderItem
import re

class NeiMengGuSpider(scrapy.Spider):
    # ok
    name = "neimenggu"

    def start_requests(self):
        yield scrapy.Request('http://www.nmgggzyjy.gov.cn/jyxx/jsgcZbgg?currentPage=1')
        yield scrapy.Request('http://www.nmgggzyjy.gov.cn/jyxx/zfcg/cggg?currentPage=1')
        yield scrapy.Request('http://www.nmgggzyjy.gov.cn/jyxx/tdAndKq/toCrggPage?currentPage=1')
        yield scrapy.Request('http://www.nmgggzyjy.gov.cn/jyxx/qtjy/jygg?currentPage=1')

    def parse(self, response):
        contents = response.xpath('//table//tr')[1:]
        for content in contents:
            title = content.xpath('.//td[3]/a/text()').extract()
            date = content.xpath('.//td[4]/text()').extract()
            short_url = content.xpath('.//td[3]/a/@href').extract_first()
            detail_url = response.urljoin(short_url)
            if "jsgcZbgg" in response.url:
                content_type = "02"
            elif "zfcg" in response.url:
                content_type = "01"
            elif "tdAndKq" in response.url:
                content_type = "03"
            else:
                content_type = "04"
            yield GovernmentSpiderItem(title=title,date=date, detail_url=detail_url,area_code="NEIMENGGU", content_type=content_type, publish_id= "181818", thing_id="42")


        max_page = response.xpath('//div[@class="page"]/div[@class="mmggxlh"]/a/text()')[-2].extract()

        for i in range(2, int(max_page)+1):
            next_url = re.sub(r'currentPage=[1-9]\d*', 'currentPage=' + str(i), response.url)
            yield scrapy.Request(next_url)




