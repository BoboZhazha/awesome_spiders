# -*- coding:utf-8 -*-

from government_spider.items import GovernmentSpiderItem
import scrapy
import json

class HeBeiSpider(scrapy.Spider):
    name = "hebei"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
    results = {"003005001": "01", "003005002": "02", "003005004": "03", "003005005": "04"}
    def start_requests(self):

        url = 'http://www.hebpr.cn/inteligentsearch/rest/inteligentSearch/getFullTextDataNew'
        #requests = []


        for k in self.results:
            formdata1 = {"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":True,"likeType":2,"equal":"%s"%k}],"time":None,"highlights":"title","statistics":None,"unionCondition":None,"accuracy":"","noParticiple":"0","searchRange":None,"isBusiness":1}
            formdata = json.dumps(formdata1)
            request = scrapy.Request(url=url, method='POST', body=formdata ,headers=self.headers, callback=self.parse, dont_filter=False)
            #requests.append(request)
        #return requests
            yield request


    def parse(self, response):
        url = 'http://www.hebpr.cn/inteligentsearch/rest/inteligentSearch/getFullTextDataNew'
        max_counts = json.loads(response.text)["result"]["totalcount"]
        datas = json.loads(response.text)["result"]["records"]
        for data in datas:
            hbitem = GovernmentSpiderItem()
            hbitem["title"] = data["title"]
            hbitem["date"] = data["showdate"]
            hbitem["detail_url"] = "http://www.hebpr.cn" + data["linkurl"]
            hbitem["area_code"] = "HEBEI"
            hbitem["publish_id"] = "181818"
            hbitem["thing_id"] = "42"
            if "003005001" in hbitem["detail_url"]:
                hbitem["content_type"] = "01"
            elif "003005002" in hbitem["detail_url"]:
                hbitem["content_type"] = "02"
            elif "003005004" in hbitem["detail_url"]:
                hbitem["content_type"] = "03"
            else:
                hbitem["content_type"] = "04"

            yield hbitem

        for i in range(10, max_counts+10, 10):
            for w in self.results:
                formdata2 = {"token":"","pn":i,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":True,"likeType":2,"equal":w}],"time":None,"highlights":"title","statistics":None,"unionCondition":None,"accuracy":"","noParticiple":"0","searchRange":None,"isBusiness":1}
                formdata = json.dumps(formdata2)
                yield scrapy.Request(url=url, method='POST', body=formdata ,headers=self.headers, callback=self.parse, dont_filter=False)










