# -*- coding: utf-8 -*-
import scrapy
from government_spider.items import GovSpiderItem
import re

# w 地区:高风
# 2019-02-25 发现这个网站是屏蔽状态, 无法爬取
class GaopingSpider(scrapy.Spider):
    name = "gaoping"
    base_url = 'http://www.gpzfcg.gov.cn/Article/ShowClass.asp?ClassID=13'

    def start_requests(self):
        yield scrapy.Request('http://www.gpzfcg.gov.cn/Article/ShowClass.asp?ClassID=13')



    def parse(self, response):
        total_page = response.xpath('//div[@class="showpage"]//a').extract()
        page_str = total_page[len(total_page)-1]
        total_re = re.match(".*?page=(\d+)",page_str)
        max_page_num = int(total_re.group(1))

        all_tr = response.xpath('//td[@class="lmlb"]//tr')
        for tr in all_tr:
            title = tr.xpath('.//a/text()').extract_first()
            detail_url = tr.xpath('.//a/@href').extract_first()
            title_str = tr.xpath('.//a').extract_first()
            try:
                match_re = re.match('.*?([0-9]{4}/[0-9]{0,2}/[0-9]{0,2} \d{1,2}:\d{1,2}:\d{1,2})', title_str, re.S)
            except Exception:
                print(title_str)
            if match_re:
                date_time = str(match_re.group(1))
            else:
                date_time = '9999/99/99 00:00:00'

            content_type = "04"
            yield GovSpiderItem(title=title, date=date_time, detail_url=detail_url, area_code="GAOPING", content_type=content_type, publish_id="181818", thing_id="42")

        for page in range(2, int(max_page_num) + 1):
            next_url =self.base_url + '&page=' + str(page)
            yield scrapy.Request(url=next_url)


