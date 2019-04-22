# -*- coding: utf-8 -*-
import scrapy
import json

# 石家庄
from government_spider.items import GovSpiderItem


class ShijiazhuanSpider(scrapy.Spider):
    name = 'shijiazhuan'
    url = "http://www.hebpr.cn/inteligentsearch/rest/inteligentSearch/getFullTextDataNew"

    def start_requests(self):

        data = {"token":"","pn":10,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001;002","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"infoc","isLike":True,"likeType":2,"equal":"1301"}],"time":None,"highlights":"title","statistics":None,"unionCondition":None,"accuracy":"","noParticiple":"0","searchRange":None,"isBusiness":1}
        d = json.dumps(data)
        return [scrapy.Request(self.url,body=d)]


    def parse(self, response):


        res = json.loads(response.text)
        total = res['result']['totalcount']
        total = 10

        for i in range((total//10) + 1):
            data_temp = {"token": "", "pn": i *10, "rn": 10, "sdt": "", "edt": "", "wd": "", "inc_wd": "", "exc_wd": "",
                         "fields": "title", "cnum": "001;002",
                         "sort": "{\"showdate\":\"0\"}", "ssort": "title", "cl": 200, "terminal": "",
                         "condition": [{"fieldName": "infoc", "isLike": True, "likeType": 2, "equal": "1301"}],
                         "time": None, "highlights": "title", "statistics": None, "unionCondition": None,
                         "accuracy": "", "noParticiple": "0", "searchRange": None, "isBusiness": 1}
            d = json.dumps(data_temp)
            yield scrapy.Request(self.url, body=d, callback=self.parse_item)

    def parse_item(self,response):
        res = json.loads(response.text)
        base_url = 'http://www.hebpr.cn'
        for i in res['result']['records']:
            title = i['title']
            detail_url = base_url + i['linkurl']
            area_code = i['zhuanzai']
            date = i['showdate']
            content_type = '01'
            yield GovSpiderItem(notice_title=title, notice_date=date, detail_url=detail_url, area_code=area_code,
                            content_type=content_type, publish_id="130100", thing_type_id="88")



