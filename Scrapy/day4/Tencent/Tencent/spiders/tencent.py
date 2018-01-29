# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = [
        'https://hr.tencent.com/position.php?lid=2156&tid=87&keywords=python']

    def parse(self, response):
        trs = response.xpath("//tr")
        for tr in trs[1:11]:
            item = TencentItem()
            tds = tr.xpath("./td")
            # 1.职位名称
            item['position_name'] = tds[0].xpath('./a/text()').extract_first()
            # 2.职位类别
            item['position_categroy'] = tds[1].xpath(
                './text()').extract_first()
            # 3.职位人数
            item['position_number'] = tds[2].xpath('./text()').extract_first()
            # 4.职位地点
            item['position_location'] = tds[3].xpath(
                './text()').extract_first()
            # 5.发布时间
            item['position_time'] = tds[4].xpath('./text()').extract_first()
            # 6.职位详情
            item['position_url'] = tds[0].xpath('./a/@href').extract_first()
            # print(item)
            yield item
        for href in response.xpath('//*[@id="next"]/@href'):
            if href:
                url = response.urljoin(href.extract())
                yield scrapy.Request(url, callback=self.parse)
