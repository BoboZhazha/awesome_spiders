# -*-coding:utf-8 -*-

from government_spider.items import GovSpiderItem
import scrapy
import re

# 有问题, 没有进入item
class JiangXiSpider(scrapy.Spider):
    name = "jiangxi"
    def start_requests(self):
        yield scrapy.Request('http://www.jxsggzy.cn/web/jyxx/002001/1.html')
        yield scrapy.Request('http://www.jxsggzy.cn/web/jyxx/002006/1.html')
        yield scrapy.Request('http://www.jxsggzy.cn/web/jyxx/002007/1.html')
        yield scrapy.Request('http://www.jxsggzy.cn/web/jyxx/002005/1.html')

    def parse(self, response):
        max_page_temp = response.xpath('//ul[@class="wb-page-items clearfix"]/li[@class="wb-page-li"]/span/text()').extract_first()
        max_page = max_page_temp.split('/')[1]
        contents = response.xpath('div[@class="ewb-infolist"]/ul')
        for content in contents:
            title = content.xpath('.//a[@class="ewb-list-name"]/text()').extract_first()
            date = content.xpath('.//span[@class="ewb-list-date"]/text()').extract_first()
            short_url = content.xpath('.//a[@class="ewb-list-name"]/@href').extract_first()
            detail_url = response.urljoin(short_url)
            if "002001" in response.url:
                content_type = "02"
            elif "002006" in response.url:
                content_type = "01"
            elif "002007" in response.url:
                content_type = "03"
            else:
                content_type = "04"
            yield GovSpiderItem(notice_title=title, notice_date=date, detail_url=detail_url, area_code="江西", content_type=content_type, publish_id= "360000", thing_type_id="88")

        for page in range(2, int(max_page)+1):
            next_url = re.sub(r'[1-9]\d*.html', str(page)+".html", response.url)
            yield scrapy.Request(url=next_url)
