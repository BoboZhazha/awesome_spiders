# -*- coding: utf-8 -*-

from government_spider.items import GovernmentSpiderItem
import scrapy
import re

# 从日志上来看是没问题的
class GuiZhouSpider(scrapy.Spider):
    name = "guizhou"
    def start_requests(self):
        yield scrapy.Request('http://www.gzsggzyjyzx.cn/jygkjsgc/index_1.jhtml')
        yield scrapy.Request('http://www.gzsggzyjyzx.cn/jygkzfcg/index_1.jhtml')
        yield scrapy.Request('http://www.gzsggzyjyzx.cn/jygkkyq/index_1.jhtml')
        yield scrapy.Request('http://www.gzsggzyjyzx.cn/jygkgycq/index_1.jhtml')

    def parse(self, response):
        max_page_temp = response.xpath('//ul[@class="pages-list"]/li[1]/a/text()').extract_first()
        max_page1 = max_page_temp.split('/')[1]
        index = max_page1.find(u'页')
        max_page = max_page1[:index]
        contents = response.xpath('//div[@class="article_listbox"]/ul[@id="listbox"]/li')
        for content in contents:
            title = content.xpath('.//div[@class="content_left"]/a/text()').extract_first()
            date = content.xpath('.//div[@class="content_right"]/span/text()').extract_first()
            detail_url = content.xpath('.//div[@class="content_left"]/a/@href').extract_first()
            if "jygkjsgc" in response.url:
                content_type = "02"
            elif "jygkzfcg" in response.url:
                content_type = "01"
            elif "jygkkyq" in response.url:
                content_type = "03"
            else:
                content_type = "04"
            yield GovernmentSpiderItem(title=title,date=date, detail_url=detail_url,area_code="GUIZHOU", content_type=content_type, publish_id= "181818", thing_id="42")
        for page in range(2, int(max_page)+1):
            next_url = re.sub(r'index_[1-9]\d*', 'index_'+str(page), response.url)
            yield scrapy.Request(url=next_url)

