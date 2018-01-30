# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    '''
    内容 content 
    作者 author 
    标签 tags
    '''
    content = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
