# -*- coding: utf-8 -*-

from government_spider.items import GovSpiderItem
import scrapy


class XinJiangSpider(scrapy.Spider):
    # 问题是构建了空的item
    name = "xinjiang"

    def start_requests(self):
        yield scrapy.Request('http://ggzy.xjbt.gov.cn/TPFront/jyxx/004001/004001002/')
        yield scrapy.Request('http://ggzy.xjbt.gov.cn/TPFront/jyxx/004002/004002006/')
        yield scrapy.Request('http://ggzy.xjbt.gov.cn/TPFront/jyxx/004004/004004001/')
        yield scrapy.Request('http://ggzy.xjbt.gov.cn/TPFront/jyxx/004003/004003002/')

    def parse(self, response):
        max_page_temp = response.xpath('//table[@algin="center"]/tr/td[@class="huifont"]/text()').extract_first()
        max_page = max_page_temp.split('/')[1]
        contents = response.xpath('//table[@width="98%"]//tr')
        for content in contents:
            title = content.xpath('.//td[2]/a/@title').extract_first()
            date = content.xpath('.//td[3]/text()').extract_first()
            if date:
                date=date[1:-1]
            else:
                date = '2018-04-22'
            short_url =content.xpath('.//td[2]/a/@href').extract_first()
            detail_url = response.urljoin(short_url)
            if "004001002" in response.url:
                content_type = "02"
            elif "004002006" in response.url:
                content_type = "01"
            elif "004004001" in response.url:
                content_type = "03"
            else:
                content_type = "04"
            yield GovSpiderItem(notice_title=title,notice_date=date, detail_url=detail_url,area_code="新疆", content_type=content_type, publish_id="650000", thing_type_id="88")
        for page in range(2, int(max_page)+1):
            next_url = response.urljoin('?Paging='+str(page))
            yield scrapy.Request(url=next_url)
