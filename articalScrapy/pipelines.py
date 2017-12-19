# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline

class ArticalscrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class  ArticleImagePipeline(ImagesPipeline):   #继承ImagePipeline
    def item_completed(self, results, item, info):
        for ok,value in results:
            image_file_path = value['path']   # 取出图片存储路径
            item['front_img_path']=image_file_path  #将图片存储路径存入item中
        return item