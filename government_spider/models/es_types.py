#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-08 10:50
# @Author  : zhangshanbo
# @File    : es_types.py
# @Remark:


from elasticsearch_dsl import DocType, Date, Nested, Boolean, analyzer, Completion, Keyword, Text, Integer
from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["http://129.28.122.49:9200/"])


# 注意集成DocType
class ArticleType(DocType):
    notice_title = Text(analyzer="ik_max_word")
    notice_date = Date()
    detail_url = Keyword()
    area_code = Keyword()
    content_type = Keyword()
    publish_id = Keyword()
    thing_type_id = Keyword()

    class Meta:
        index = "gov_spiders"
        doc_type = "article"


if __name__ == '__main__':
    ArticleType.init()