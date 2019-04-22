# -*-coding:utf-8 -*-

import scrapy
from government_spider.items import GovSpiderItem
import re

# 这个因为detail为none报错, 需要重新验证一下
class HaiNanSpider(scrapy.Spider):
    name = "hainan"
    def start_requests(self):
        yield scrapy.Request('http://zw.hainan.gov.cn/ggzy/ggzy/jgzbgg/index_1.jhtml')
        yield scrapy.Request('http://zw.hainan.gov.cn/ggzy/ggzy/cggg/index_1.jhtml')
        yield scrapy.Request('http://zw.hainan.gov.cn/ggzy/ggzy/crgg/index_1.jhtml')

    def parse(self, response):
        max_page = response.xpath('//div[@class="pagesite"]/div//option/text()')[-1].extract()

        contents = response.xpath('//table[@class="newtable"]//tr')[:-1]
        for content in contents:
            title = content.xpath('.//td[3]/a/text()').extract_first()
            date = content.xpath('.//td[4]/text()').extract_first()
            detail_url = content.xpath('.//td[3]/a/@href').extract_first()

            if "jgzbgg" in response.url:
                content_type = "02"
            elif "cggg" in response.url:
                content_type = "01"
            else:
                content_type = "03"
            yield GovSpiderItem(notice_title=title, notice_date=date, detail_url=detail_url, area_code="海南", content_type=content_type, publish_id= "150303", thing_type_id="88")

        for i in range(2, int(max_page)+1):
            next_url = re.sub(r'index_[1-9]\d*', "index_" + str(i), response.url)
            yield scrapy.Request(next_url)