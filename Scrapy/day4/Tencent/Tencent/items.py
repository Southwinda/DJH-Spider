# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 1.职位名称
    position_name = scrapy.Field()
    # 2.职位类别
    position_categroy = scrapy.Field()
    # 3.职位人数
    position_number = scrapy.Field()
    # 4.职位地点
    position_location=scrapy.Field()
    # 5.发布时间
    position_time=scrapy.Field()
    # 6.职位详情
    position_url=scrapy.Field()
