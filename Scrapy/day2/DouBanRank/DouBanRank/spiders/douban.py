# -*- coding: utf-8 -*-
import scrapy
from DouBanRank.items import DoubanrankItem
import json

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/ithil_j/activity/movie_annual2017/widget/1']

    def parse(self, response):
        items=[]
        data=json.loads(response.body.decode('utf-8'))
        subjects=data['res']['subjects']
        ranking=0
        for subject in subjects:
            item=DoubanrankItem()
            item['ranking']=ranking+1
            item['title']=subject['title']
            item['rating'] =subject['rating']
            item['cover']=subject['cover']
            item['rating_count']=subject['rating_count']
            items.append(item)
            
        return items
