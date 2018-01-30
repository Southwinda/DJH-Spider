# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class DouyuPipeline(ImagesPipeline):
    '''
    下载保存图片
    '''

    def process_item(self, item, spider):
        return item

    def get_media_requests(self, item, info):
        '''
        根据图片url构造请求
        '''
        vertical_src = item['vertical_src']
        yield Request(vertical_src)

    def item_completed(self, results, item, info):
        ok, x = results
        if not x:
            raise DropItem("Item contains no images")
        return item
