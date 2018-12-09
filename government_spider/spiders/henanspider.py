# -*- coding: utf-8 -*-

from government_spider.items import GovernmentSpiderItem
import scrapy


class HnSpider(scrapy.Spider):
    name = 'henan'
    def start_requests(self):
        yield scrapy.Request(url='http://www.hnggzy.com/hnsggzy/jyxx/002001/002001001/')
        yield scrapy.Request(url='http://www.hnggzy.com/hnsggzy/jyxx/002002/002002001/')
        yield scrapy.Request(url='http://www.hnggzy.com/hnsggzy/jyxx/002005/002005001/')

    def parse(self, response):
        max_page_temp = response.xpath('//div[@class="pagemargin"]//td[@class="huifont"]/text()').extract_first()
        max_page = max_page_temp.split('/')[1]
        contents = response.xpath('//table[@width="100%"]/tr[@height="27"]')
        for content in contents:
            title = content.xpath('.//td[2]/a/text()').extract_first()
            date = content.xpath('.//td[3]/font/text()').extract_first()
            short_url = content.xpath('.//td[2]/a/@href').extract_first()
            detail_url = response.urljoin(short_url)
            if "002001001" in response.url:
                content_type = "02"
            elif "002002001" in response.url:
                content_type = "01"
            else:
                content_type = "04"
            yield GovernmentSpiderItem(title=title,date=date, detail_url=detail_url,area_code="HENAN", content_type=content_type, publish_id= "181818", thing_id="42")
        for page in range(2, int(max_page)+1):
            next_url = response.urljoin('?Page='+str(page))
            yield scrapy.Request(url=next_url)

