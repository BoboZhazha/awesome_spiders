# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GovernmentSpiderItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    detail_url = scrapy.Field()
    area_code = scrapy.Field()
    content_type = scrapy.Field()
    publish_id = scrapy.Field()
    thing_id = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
                insert into gov_notice(notice_title, notice_date, detail_url, area_code, content_type, publish_id, thing_type_id) VALUES 
                (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE notice_title=VALUES(notice_title)
            """
        params = (
        self["title"], self['date'], self["detail_url"], self["area_code"], self["content_type"], self["publish_id"],self["thing_id"])

        return insert_sql, params


