# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import codecs
import json
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi

import MySQLdb
import MySQLdb.cursors

class ArticalscrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonEncodingPipeline(object):
    #自定义json文件的导出
    def __init__(self):
        self.file= codecs.open('article.json','w',encoding="utf-8")  # 'w'是write的意思
    def process_item(self, item, spider):
        lines= json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(lines)
        return item
    def spider_closed(self, spider):
        self.file.close()

class JsonExporterPipeline(object):
    #调用scrapy提供的json exporter导出json文件
    def __init__(self):
        self.file= open("articleexporter.json","wb")  # "wb"的意思是以二进制的形式打开
        self.exporter =JsonItemExporter(self.file,encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class MysqlPipeline(object):
    #采用同步的机制写入mysql
    def __init__(self):
        self.conn= MySQLdb.connect("192.168.0.114","root","xjl1994920","articlespider", 3336, charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql="""
            insert into article(title,url,create_date,fav_nums)
            VALUES (%s,%s,%s,%s)
        """
        self.cursor.execute(insert_sql,(item["title"],item["url"],item["create_date"],item["fav_nums"]))
        self.conn.commit()
        return item

class MysqlTwistedPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):  # 读入setting.py文件中的mysql配置
        dbparams=dict(host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            port = settings["MYSQL_PORT"],
            charset='utf8',
            cursorclass =MySQLdb.cursors.DictCursor,
             use_unicode=True)

        dbpool= adbapi.ConnectionPool("MySQLdb", **dbparams)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步
        query= self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_error)  # 处理异常

    def handle_error(self,failure):
        # 处理异步插入的错误
        print(failure)

    def do_insert(self,cursor,item):
        # 执行具体插入
        insert_sql = """
                    insert into article(title,url,create_date,fav_nums,comment_nums,praise_nums,tag,content,front_img_url,url_object_id)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
        cursor.execute(insert_sql, (item["title"], item["url"], item["create_date"],item["fav_nums"],item["comment_nums"],
                                    item["praise_nums"],item["tags"],item["content"],item["front_img_url"],item["url_object_id"]))


class  ArticleImagePipeline(ImagesPipeline):   #继承ImagePipeline
    def item_completed(self, results, item, info):
        if "front_img_path" in item:  # 判断"front_img_path"是否存在
            for ok,value in results:
                image_file_path = value['path']   # 取出图片存储路径
                item['front_img_path']=image_file_path  #将图片存储路径存入item中
            return item