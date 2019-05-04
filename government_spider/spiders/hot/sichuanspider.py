# -*-coding:utf-8 -*-

import scrapy
from government_spider.items import GovSpiderItem
import json


# 2019.5.3重写, 网站有很多数据,我就取了最近3个月的,
class SiChuanSpider(scrapy.Spider):
    # 这里的名字
    name = "sichuan"

    headers = {
        'Origin': 'http://ggzyjy.sc.gov.cn',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://ggzyjy.sc.gov.cn/jyxx/002002/17.html',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    url_template = 'http://58.87.81.13/Info/GetInfoListNew?keywords=&times=4&page={}'

    # times=4是最近3个月的, 6是时间的类型,本来打算从2018年的5月1号开始爬, 再久远的数据不要了. 感觉不需要
    def start_requests(self):
        yield scrapy.Request(url='http://58.87.81.13/Info/GetInfoListNew?keywords=&times=4&page=1', headers=self.headers)

    #
    def parse(self, response):
        pageCount = json.loads(response.text)['pageCount']
        for page in range(pageCount+1):
            current_url = self.url_template.format(page)
            yield scrapy.Request(url=current_url, headers=self.headers, callback=self.parse_detail)


    # 拿到url, 得到总页数
    def parse_detail(self, response):
        data = json.loads(response.text)['data']
        res = json.loads(data)
        base_url = 'http://58.87.81.13/Info/ProjectDetail'
        for i in res:
            title = i['Title']
            notice_date = i['CreateDate']
            detail_url = base_url + i['Link']
            area_code = i['username']
            businessType = i['businessType']
            if businessType == '工程建设':
                content_type = '01'
            elif businessType == '工程建设':
                content_type = '03'
            elif businessType == '政府采购':
                content_type = '02'

        yield GovSpiderItem(notice_title=title, notice_date=notice_date, detail_url=detail_url, area_code=area_code,
                            content_type=content_type, publish_id="530000", thing_type_id="88",source = 'sichuanspider')
