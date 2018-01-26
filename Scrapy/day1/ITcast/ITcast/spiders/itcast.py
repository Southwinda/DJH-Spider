# -*- coding: utf-8 -*-
import scrapy
from ITcast.items import ItcastItem


# 命令行命令
# scrapy crawl 运行spider
# -o 表示输出：输出支持：the supported list ('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')
# json,jsonlines 默认unicode
# pickle,marshal 二进制
# scrapy crawl itcast -o output.json


# XPath对象：Selector对象
# 四个基本方法：
# xpath():传入xpath表达式，返回表达式对应的所有节点的selector list列表
# extract():系列化该节点为Unicode字符串并返回list
# css():传入css表达式，返回该表达时所对应的所有节点的selector list列表，语法同beautifulsoup
# 


class ItcastSpider(scrapy.Spider):
    # 爬虫名字（必须参数）
    name = 'itcast'
    # 爬虫域名范围（可选参数，作为url列表的参考前提，可不写）
    allowed_domains = ['http://www.itcast.cn/']
    # 爬虫执行起始的第一批url列表（必须参数）
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        print('djh:ItcastSpider...parse()')
        node_list = response.xpath("//div[@class='li_txt']")

        items = []
        for node in node_list[:5]:
            # 创建item对象
            item = ItcastItem()

            # 老师姓名
            item['name'] = node.xpath(
                "./h3/text()").extract()[0]  # xpath对象转list
            # 老师职称
            item['title'] = node.xpath(
                "./h4/text()").extract()[0]  # xpath对象转list
            # 老师信息
            item['info'] = node.xpath(
                "./p/text()").extract()[0]  # xpath对象转list

            items.append(item)

        return items
