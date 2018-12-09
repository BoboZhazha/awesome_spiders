# -*- coding: utf-8 -*-

from government_spider.items import GovernmentSpiderItem
import scrapy
import re


class ShaanXiSpider(scrapy.Spider):
    # 完成
    name = "shaanxi"

    def start_requests(self):
        yield scrapy.Request('http://www.sxggzyjy.cn/jydt/001001/001001001/1.html')
        yield scrapy.Request('http://www.sxggzyjy.cn/jydt/001001/001001004/1.html')
        yield scrapy.Request('http://www.sxggzyjy.cn/jydt/001001/001001002/1.html')
        yield scrapy.Request('http://www.sxggzyjy.cn/jydt/001001/001001005/1.html')

    def parse(self, response):
        max_page_temp = response.xpath('//ul[@class="ewb-page-items clearfix"]/li[@class="ewb-page-li ewb-page-noborder ewb-page-num"]/span/text()').extract_first()
        max_page = max_page_temp.split('/')[1]
        # max_page = 3
        contents = response.xpath('//ul[@class="ewb-list"]/li')
        for content in contents:
            title = content.xpath('.//a[@class="ewb-list-name ewb-otw"]/text()').extract_first()
            date =  content.xpath('.//span[@class="ewb-list-date"]/text()').extract_first()
            short_url = content.xpath('.//a[@class="ewb-list-name ewb-otw"]/@href').extract_first()
            detail_url = response.urljoin(short_url)
            if "001001001" in response.url:
                content_type = "02"
            elif "001001004" in response.url:
                content_type = "01"
            elif "001001002" in response.url:
                content_type = "03"
            else:
                content_type = "04"
            yield GovernmentSpiderItem(title=title,date=date, detail_url=detail_url,area_code="SHAANXI", content_type=content_type, publish_id= "181818", thing_id="42")
        for page in range(2, int(max_page)+1):
            next_url = re.sub(r'[1-9]\d*.html', str(page)+'.html', response.url)
            yield scrapy.Request(url=next_url)