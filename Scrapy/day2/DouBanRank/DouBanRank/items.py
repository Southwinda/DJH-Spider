# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanrankItem(scrapy.Item):
    #排名
    ranking=scrapy.Field()
    #海报
    cover=scrapy.Field()
    #名称
    title=scrapy.Field()
    #评分
    rating=scrapy.Field()
    #评分人数
    rating_count=scrapy.Field()