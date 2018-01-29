# -*- coding: utf-8 -*-
import scrapy

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?lid=2156&tid=87&keywords=python']

    def parse(self, response):
        pass 
