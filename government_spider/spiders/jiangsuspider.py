# -*- coding:utf-8 -*-

import scrapy
from government_spider.items import GovernmentSpiderItem
import json

class JiangSuSpider(scrapy.Spider):
    name = "jiangsu"

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01'}
    def start_requests(self):
        url = 'http://jsggzy.jszwfw.gov.cn/jyxx/tradeInfonew.html'


        result = {"003001":"02", "00304":"01", "003005":"03", "003009":"04"}
        for k in result:
            formdata1 = {"token":"","pn":0,"rn":"15","sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"infodatepx\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":True,"likeType":2,"equal":"%s"%k},{"fieldName":"fieldvalue","isLike":True,"likeType":2,"equal":"省级"}],"time":None,"highlights":"title","statistics":None,"unionCondition":None,"accuracy":"","noParticiple":"0","searchRange":None,"isBusiness":"1"}
            formdata = json.dumps(formdata1)
            yield scrapy.Request(url=url, method='POST', body=formdata ,headers=self.headers, callback=self.parse, dont_filter=False, meta={k:result[k]})

    def parse(self, response):
        url = 'http://jsggzy.jszwfw.gov.cn/jyxx/tradeInfonew.html'
        max_counts = json.loads(response.text)["result"]["totalcount"]
        for i in range(15, max_counts, 15):
            formdata1 = {"token":"","pn":i,"rn":"15","sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"infodatepx\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":True,"likeType":2,"equal":"%s"%response.meta.keys()[0]},{"fieldName":"fieldvalue","isLike":True,"likeType":2,"equal":"省级"}],"time":None,"highlights":"title","statistics":None,"unionCondition":None,"accuracy":"","noParticiple":"0","searchRange":None,"isBusiness":"1"}
            formdata = json.dumps(formdata1)
            yield scrapy.Request(url=url, method='POST', body=formdata ,headers=self.headers, callback=self.parse, dont_filter=False, meta=response.meta)

        datas = json.loads(response.text)["result"]["records"]
        for data in datas:
            item = GovernmentSpiderItem()
            item["title"] = data["title"]
            item["date"] = datas["infodateformat"]
            item["area_code"] = "JIANGSU"
            item["publish_id"] = "181818"
            item["thing_id"] = "42"
            if response.meta.has_key("003001") == True:
                item["content_type"] = "02"
            elif response.meta.has_key("003004") == True:
                item["content_type"] = "01"
            elif response.meta.has_key("003005") == True:
                item["content_type"] = "03"
            else:
                item["content_type"] = "04"
            yield item




