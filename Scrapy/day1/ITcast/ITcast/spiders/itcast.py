# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    #爬虫名字
    name = 'itcast'
    #爬虫域名范围
    allowed_domains = ['http://www.itcast.cn/']
    #爬虫请求url列表
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        print('ItcastItem(scrapy.Item)......')
        #老师姓名
        name = response.xpath()
        #老师职称
        title = response.xpath()
        #老师信息
        indo = response.xpath()
        