# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import codecs
import json
from scrapy.exporters import JsonItemExporter

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

class  ArticleImagePipeline(ImagesPipeline):   #继承ImagePipeline
    def item_completed(self, results, item, info):
        for ok,value in results:
            image_file_path = value['path']   # 取出图片存储路径
            item['front_img_path']=image_file_path  #将图片存储路径存入item中
        return item