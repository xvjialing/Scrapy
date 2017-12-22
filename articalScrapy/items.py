# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst,Join
from scrapy.loader import ItemLoader
import datetime
import re


class ArticalscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y%M%D").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()

    return create_date

def nums_convert(value):
    re_match = re.match(".*(\d+).*", value)
    if re_match:
        nums = int(re_match.group(1))
    else:
        nums = 0

    return nums

def tags_convert(value):
    if "评论" in value:
        return ""
    else:
        return value

def return_value(value):
    return value

class ArticleItemLoader(ItemLoader):
    # 自定义ItemLoader
    default_output_processor = TakeFirst()


class JobBoleArticleItem(scrapy.Item):
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_img_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    front_img_path = scrapy.Field()
    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor = MapCompose(date_convert)
    )
    praise_nums = scrapy.Field(
        input_processor=MapCompose(nums_convert)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(nums_convert)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(nums_convert)
    )
    content = scrapy.Field()
    tags = scrapy.Field(
        input_processor=MapCompose(tags_convert),
        output_processor=Join(",")
    )
