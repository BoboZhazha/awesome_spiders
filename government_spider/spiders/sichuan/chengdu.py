# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request

class ChengduSpider(scrapy.Spider):
    name = 'chengdu'



    # 这个网站就4类
    def start_requests(self):
        yield scrapy.Request(
            url='https://www.cdggzy.com/site/JSGC/List.aspx')


    def parse(self, response):
        max_page_temp = response.xpath('//div[@id="pagination"]//a[last()]/@href').extract()[1]
        max_page = re.match(r".*?'(\d+)'", max_page_temp).group(1)
        __VIEWSTATE = response.xpath("//input[@id='__VIEWSTATE']/@value")

        data = {
            'ctl00$ScriptManager1': 'ctl00$ContentPlaceHolder1$UpdatePanel1|ctl00$ContentPlaceHolder1$Pager',
            'ctl00$ContentPlaceHolder1$displaytypeval': '0',
            'ctl00$ContentPlaceHolder1$displaystateval': '0',
            'ctl00$ContentPlaceHolder1$dealaddressval': '0',
            'ctl00$ContentPlaceHolder1$keyword': '',
            '__VIEWSTATE': __VIEWSTATE,
            '__VIEWSTATEGENERATOR': '9F052A18',
            '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$Pager',
            '__EVENTARGUMENT': '6',
            '__EVENTVALIDATION': '/wEdAAiCz+zCyBm2YkUQH5FPdp2bZXbjphD4J6Ci0P2UUXCmZQp8fmeAe3E+Z+lyrRcok/uWwC8UtjR1ulKkYi2xiF6rZi7H72kkAvPqROrOG28FXID8g/xeCzDZJOPgpGV4zViznYSIw3B963y/xzaOhgoHdty0mXvz7f+9YtBAL8kV3eXPVWiCSZFq8DHXi2Q7/kFw3A2X',
            '__ASYNCPOST': 'true',
        }


        # for i in range(int(max_page)):
        #     self.data['__EVENTARGUMENT'] = str(i)
        #     yield scrapy.FormRequest(url=response.url, formdata=self.data, callback=self.parse_item)
        yield scrapy.FormRequest(url="https://www.cdggzy.com/site/JSGC/List.aspx", method = 'POST', formdata=data, callback=self.parse_item)

    def parse_item(self, response):
        contents = response.xpath("//div[@id='contentlist']//a[@id='linkbtnSrc']")
        for content in contents:
            title = content.xpath(".//text()").get()
            href = response.xpath(".//href").get()




        # max_page = json.loads(response.text)["pagination"]
        #
        # datas = json.loads(response.text)["data"]
        # datas1 = json.loads(datas)
        # item = GovSpiderItem()
        # for data in datas1:
        #
        #     item["notice_title"] = data["Title"]
        #     item["notice_date"] = data["CreateDateStr"]
        #     item["detail_url"] = "http://ggzyjy.sc.gov.cn" + str(data["Link"])
        #     item["area_code"] = "四川"
        #     item["publish_id"] = "510000"
        #     item["thing_type_id"] = "88"
        #     if "project" in response.url:
        #         item["content_type"] = "02"
        #     elif "purchase" in response.url:
        #         item["content_type"] = "01"
        #     elif "land" in response.url:
        #         item["content_type"] = "03"
        #     else:
        #         item["content_type"] = "04"
        #     yield item
        #
        # for i in range(2, max_page + 1):
        #     next_url = re.sub(r'page=[1-9]\d*', 'page=' + str(i), response.url)
        #     yield scrapy.Request(next_url)