# -*-coding:utf-8 -*-
import scrapy
from government_spider.items import GovSpiderItem
import json


# 2019-02-25 爬取有问题
class GuangDongSpider(scrapy.Spider):
    name = "guangdong"
    k = {"30091": "03", "30011": "01", "200122": "02"}

    def start_requests(self):

        for i in self.k:
            formdata = {"currPage":"1", "typeId":i, "pageSize":"20"}

            url = 'http://www.gdggzy.org.cn/prip-portal-web/main/viewList.do'
            yield scrapy.FormRequest(url=url,
                                     formdata=formdata,
                                     meta={"ss":i}
                                     )


    def parse(self, response):
        max_count_temp = response.xpath('//div[@id="TestView_pageableDiv"]/@totalsize').extract_first()
        max_count = int(max_count_temp)

        if max_count <= 20:
            max_page = max_count
        elif max_count%20 == 0:
            max_page = max_count/20
        else:
            max_page = max_count/20 + 1


        contents = response.xpath('//div[@class="list_box"]/ul')
        for content in contents:
            item = GovSpiderItem()
            item['title'] = content.xpath('.//li[@class="l"]/a/@title').extract_first()
            item['date'] = contents.xpath('.//li[@class="r"]/text()').extract_first()
            short_url = content.xpath('.//li[@class="l"]/a/@href').extract_first()
            detail_url = "http://www.gdggzy.org.cn" + short_url
            item['detail_url'] = detail_url
            item['area_code'] = "GUANGDONG"
            item['publish_id'] = "181818"
            item['thing_id'] = "42"
            if "30091" == response.meta["ss"]:
                content_type = "03"
            elif "30011" in response.meta["ss"]:
                content_type = "01"
            else:
                content_type = "02"
            item["content_type"] = content_type
            yield item


        for i in range(2, max_page+1):
            for w in self.k:
                next_url = 'http://www.gdggzy.org.cn/prip-portal-web/main/viewList.do'
                formdata = {"currPage":str(i), "typeId": w , "pageSize":"20"}
                yield scrapy.FormRequest(url=next_url, formdata=formdata, dont_filter=False, meta={"ss": w})
