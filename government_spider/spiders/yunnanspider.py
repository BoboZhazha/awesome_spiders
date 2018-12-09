# -*- coding:utf-8 -*-

import scrapy
from government_spider.items import GovernmentSpiderItem
import re

class YunNanSpider(scrapy.Spider):
    # 完成
    name = "yunnan"
    def start_requests(self):
        yield scrapy.Request('https://www.ynggzy.com/jyxx/zfcg/cggg?currentPage=1')
        yield scrapy.Request('https://www.ynggzy.com/jyxx/jsgcZbgg?currentPage=1')
        yield scrapy.Request('https://www.ynggzy.com/jyxx/qtjy/crgg?currentPage=1')

    def parse(self, response):
        max_page = response.xpath('//div[@class="mmggxlh"]/a/text()')[-2].extract()


        contents = response.xpath('//table[@id="data_tab"]/tbody/tr')[1:]
        for content in contents:
            title = content.xpath('.//td[3]/a/@title').extract_first()
            date = content.xpath('.//td[4]/text()').extract_first()
            short_url = content.xpath('.//td[3]/a/@href').extract_first()
            detail_url ="https://www.ynggzy.com/" + short_url
            if "zfcg" in response.url:
                content_type = "01"
            elif "jsgcZbgg" in response.url:
                content_type = "02"
            else:
                content_type = "04"
            yield GovernmentSpiderItem(title=title,date=date, detail_url=detail_url,area_code="YUNNAN", content_type=content_type, publish_id= "181818", thing_id="42")


        for i in range(2, int(max_page)+1):
            next_url = re.sub(r'[1-9]\d*', str(i), response.url)
            yield scrapy.Request(next_url)






