# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class ToscrapeSpider(scrapy.Spider):
    name = 'toscrape'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/tag/love']



    def parse(self, response):

        # filename = response.url.split("/")[-1] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        
        
        
        # items = []
        # for node in response.xpath("//div[@class='col-md-8']/div[@class='quote']"):
        #     item=TutorialItem()
        #     content = node.xpath("./span[1]/text()").extract()
        #     author=node.xpath("./span[2]/small/text()").extract()
        #     tags = node.xpath('./div[@class="tags"]/a/text()').extract()
        #     item["author"]=author
        #     item["content"]=content
        #     item["tags"]=tags
        #     items.append(item)
        #     yield item
        # return items
        for node in response.xpath("//div[@class='col-md-8']/div[@class='quote']"):
            item = TutorialItem()
            item["author"]=node.xpath("./span[2]/small/text()").extract()
            item["content"]=node.xpath("./span[1]/text()").extract()
            item["tags"]=node.xpath('./div[@class="tags"]/a/text()').extract()
            yield item
        for href in response.xpath('//li[@class="next"]/a/@href'):
            if href:
                url=response.urljoin(href.extract())
                yield scrapy.Request(url,callback=self.parse_contents_of_next)

    def parse_contents_of_next(self, response):
        for node in response.xpath("//div[@class='col-md-8']/div[@class='quote']"):
            item = TutorialItem()
            item["author"]=node.xpath("./span[2]/small/text()").extract()
            item["content"]=node.xpath("./span[1]/text()").extract()
            item["tags"]=node.xpath('./div[@class="tags"]/a/text()').extract()
            yield item
        for href in response.xpath('//li[@class="next"]/a/@href'):
            if href:
                url=response.urljoin(href.extract())
                yield scrapy.Request(url,callback=self.parse_contents_of_next)
