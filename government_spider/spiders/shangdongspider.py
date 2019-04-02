# -*-coding:utf-8 -*-

import scrapy
import re
from government_spider.items import GovSpiderItem

class ShangDongSpider(scrapy.Spider):
    # 完成
    name = "shandong"
    def start_requests(self):
        yield scrapy.Request('http://www.sdggzyjy.gov.cn/queryContent_1-jyxxgg.jspx?title=&origin=&inDates=&channelId=78&ext=')
        yield scrapy.Request('http://www.sdggzyjy.gov.cn/queryContent_1-jyxxgg.jspx?title=&origin=&inDates=&channelId=79&ext=')
        yield scrapy.Request('http://www.sdggzyjy.gov.cn/queryContent_1-jyxxgg.jspx?title=&origin=&inDates=&channelId=80&ext=')
        yield scrapy.Request('http://www.sdggzyjy.gov.cn/queryContent_1-jyxxgg.jspx?title=&origin=&inDates=&channelId=83&ext=')

    def parse(self, response):
        max_page_temp = response.xpath('//ul[@class="pages-list"]/li[1]/a/text()').extract_first()
        max_page1 = max_page_temp.split('/')[1]
        index = max_page1.find(u'页')
        max_page = max_page1[:index]
        contens = response.xpath('//ul[@class="article-list-a"]/li')
        for conten in contens:
            titleList = conten.xpath('.//div[@class="article-list3-t"]/a/text()').extract()
            title = "".join(titleList)
            date = conten.xpath('.//div[@class="article-list3-t"]/div[@class="list-times"]/text()').extract_first()
            detail_url = conten.xpath('.//div[@class="article-list3-t"]/a/@href').extract_first()
            if "channelId=78" in response.url:
                content_type = "02"
            elif "channelId=79" in response.url:
                content_type = "01"
            elif "channelId=80" in response.url:
                content_type = "03"
            else:
                content_type = "04"
            yield GovSpiderItem(notice_title=title,notice_date=date, detail_url=detail_url,area_code="山东", content_type=content_type, publish_id= "370000", thing_type_id="88")
        for page in range(2, int(max_page)+1):
            next_url = re.sub(r'queryContent_\d', "queryContent_" + str(page), response.url)

            yield scrapy.Request(url=next_url)


