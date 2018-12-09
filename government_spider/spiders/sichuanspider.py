# -*-coding:utf-8 -*-

import scrapy
from government_spider.items import GovernmentSpiderItem
import json
import re

# 数据库查看文件是有10倍的重复
class SiChuanSpider(scrapy.Spider):
    # 这里的名字
    name = "sichuan"
    def start_requests(self):
        yield scrapy.Request(url='http://www.scggzy.gov.cn/Info/GetInfoListNew?keywords=&times=5&timesStart=&timesEnd=&province=&area=&businessType=project&informationType=&industryType=&page=1')
        yield scrapy.Request(url='http://www.scggzy.gov.cn/Info/GetInfoListNew?keywords=&times=5&timesStart=&timesEnd=&province=&area=&businessType=land&informationType=&industryType=&page=1')
        yield scrapy.Request(url='http://www.scggzy.gov.cn/Info/GetInfoListNew?keywords=&times=5&timesStart=&timesEnd=&province=&area=&businessType=purchase&informationType=&industryType=&page=1')
        yield scrapy.Request(url='http://www.scggzy.gov.cn/Info/GetInfoListNew?keywords=&times=5&timesStart=&timesEnd=&province=&area=&businessType=othertrade&informationType=&industryType=&page=1')

    def parse(self, response):
        max_page = json.loads(response.text)["pageCount"]

        datas = json.loads(response.text)["data"]
        datas1 = json.loads(datas)
        item = GovernmentSpiderItem()
        for data in datas1:

            item["title"] = data["Title"]
            item["date"] = data["CreateDateStr"]
            item["detail_url"] = "http://www.scggzy.gov.cn" + str(data["Link"])
            item["area_code"] = "SICHUAN"
            item["publish_id"] = "181818"
            item["thing_id"] = "42"
            if "project" in response.url:
                item["content_type"] = "02"
            elif "purchase" in response.url:
                item["content_type"] = "01"
            elif "land" in response.url:
                item["content_type"] = "03"
            else:
                item["content_type"] = "04"
            yield item

        for i in range(2, max_page+1):
            next_url = re.sub(r'page=[1-9]\d*', 'page=' + str(i) , response.url)
            yield scrapy.Request(next_url)

