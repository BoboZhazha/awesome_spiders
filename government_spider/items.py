# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GovSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    notice_title = scrapy.Field()
    notice_date = scrapy.Field()
    detail_url = scrapy.Field()
    area_code = scrapy.Field()
    content_type = scrapy.Field()
    publish_id = scrapy.Field()
    thing_type_id = scrapy.Field()
    source = scrapy.Field()




