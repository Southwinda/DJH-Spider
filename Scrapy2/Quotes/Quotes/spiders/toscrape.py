# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from Quotes.items import QuotesItem


class ToscrapeSpider(scrapy.Spider):
    name = 'toscrape'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            item = QuotesItem()
            item['content'] = quote.xpath(
                './span[@class="text"]/text()').extract_first()
            item['author'] = quote.xpath(
                './span/small[@class="author"]/text()').extract_first()
            item['tags'] = quote.xpath('./div/a/text()').extract()
            yield item
        next_href = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_href:
            next_url = response.urljoin(next_href)
            yield Request(next_url, callback=self.parse_next_page)

    def parse_next_page(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            item = QuotesItem()
            item['content'] = quote.xpath(
                './span[@class="text"]/text()').extract_first()
            item['author'] = quote.xpath(
                './span/small[@class="author"]/text()').extract_first()
            item['tags'] = quote.xpath('./div/a/text()').extract()
            yield item
        next_href = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_href:
            next_url = response.urljoin(next_href)
            yield Request(next_url, callback=self.parse_next_page)
