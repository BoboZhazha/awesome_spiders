import json


class JsonPipeline(object):
    def __init__(self):
        self.filename = open("spider.json", "wb")

    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(jsontext.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.filename.close()


from government_spider.models.es_types import ArticleType


# 数据写入到es中
class ElasticsearchPipeline(object):

    def process_item(self, item, spider):
        article = ArticleType()
        article.notice_title = item['notice_title']
        article.notice_date = item['notice_date']
        article.detail_url = item['detail_url']
        article.area_code = item['area_code']
        article.content_type = item['content_type']
        article.publish_id = item['publish_id']
        article.thing_type_id = item['thing_type_id']
        article.save()
        return item
