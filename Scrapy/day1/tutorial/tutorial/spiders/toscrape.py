# -*- coding: utf-8 -*-
import scrapy


class ToscrapeSpider(scrapy.Spider):
    name = 'toscrape'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']
    #http://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html
    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
