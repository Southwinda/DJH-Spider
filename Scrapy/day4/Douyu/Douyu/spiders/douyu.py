# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    start_urls = [
        'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=']

    def parse(self, response):
        datas = json.loads(response.body)
        for data in datas['data']:
            item = DouyuItem()
            item['vertical_src'] = data['vertical_src']
            item['nickname'] = data['nickname']
            yield item
