import pymysql
# twisted: 用于异步写入(包含数据库)的框架，cursor.execute()是同步写入
from twisted.enterprise import adbapi
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



class MysqlTwistedPipline(object):

    def __init__(self, pool):
        self.dbpool = pool

    @classmethod
    def from_settings(cls, settings):
        """
        这个函数名称是固定的，当爬虫启动的时候，scrapy会自动调用这些函数，加载配置数据。
        :param settings:
        :return:
        """
        params = dict(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],
            db=settings['MYSQL_DB'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset=settings['MYSQL_CHARSET'],
            cursorclass=pymysql.cursors.DictCursor
        )

        # 创建一个数据库连接池对象，这个连接池中可以包含多个connect连接对象。
        # 参数1：操作数据库的包名
        # 参数2：链接数据库的参数
        db_connect_pool = adbapi.ConnectionPool('pymysql', **params)

        # 初始化这个类的对象
        obj = cls(db_connect_pool)
        return obj

    def process_item(self, item, spider):
        """
        在连接池中，开始执行数据的多线程写入操作。
        :param item:
        :param spider:
        :return:
        """
        # 参数1：在线程中被执行的sql语句
        # 参数2：要保存的数据
        result = self.dbpool.runInteraction(self.insert, item)
        # 给result绑定一个回调函数，用于监听错误信息
        result.addErrback(self.error)

    def error(self, reason):
        print('--------', reason)

    # 线面这两步分别是数据库的插入语句，以及执行插入语句。这里把插入的数据和sql语句分开写了，跟何在一起写效果是一样的
    def insert(self, cursor, item):
        insert_sql = "insert into gov_notice(notice_title, notice_date, detail_url, area_code, content_type, publish_id, thing_type_id) VALUES (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE notice_title=VALUES(notice_title)"

        cursor.execute(insert_sql, (
        item['title'], item['date'], item['detail_url'], item['area_code'], item['content_type'], item['publish_id'],
        item['thing_id']))
        # 不需要commit()



