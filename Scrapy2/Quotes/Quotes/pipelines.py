# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.exceptions import DropItem
import logging


class TextPipeline(object):

    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        content = item['content']
        if content:
            if len(content) > self.limit:
                item['content'] = content[:self.limit].rstrip() + "..."
            return item
        else:
            raise DropItem("Missing Text")


class MysqlPipline(object):
    def __init__(self, mysql_user, mysql_pwd, mysql_table):
        self.mysql_user = mysql_user
        self.mysql_pwd = mysql_pwd
        self.mysql_table = mysql_table

    @classmethod
    def from_crawler(cls, crawler):
        '''
        获取配置信息，返回类对象
        '''
        return cls(
            mysql_user=crawler.settings.get('MYSQL_USER'),
            mysql_pwd=crawler.settings.get('MYSQL_PWD'),
            mysql_table=crawler.settings.get('MYSQL_TABLE')
        )

    def open_spider(self, spider):
        '''
        初始化操作
        '''
        self.conn = pymysql.connect("localhost", self.mysql_user, self.mysql_pwd,
                                    self.mysql_table, use_unicode=True, charset="utf8")
        if self.conn != None:
            logging.info('connection is success')
        else:
            logging.info('connection is not success')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # 如果表存在则删除
        self.cursor.execute("DROP TABLE IF EXISTS quotes")
        # 使用预处理语句创建表
        sql = """CREATE TABLE quotes (id  INT AUTO_INCREMENT PRIMARY KEY ,content  VARCHAR(80) ,author VARCHAR(50),tags VARCHAR(50))"""
        self.cursor.execute(sql)
        if item:
            content = item['content']
            author = item['author']
            tags = item['tags']
            sql = "INSERT INTO quotes(content,author,tags) VALUES('{}','{}','{}')".format(
                str(content), str(author), str(tags))
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                logging.info('item has been inserted in mysql!')
                return item
            except Exception as e:
                logging.error('mysql saving error!type(item)=')
        else:
            logging.info('item is None!')

    def close_spider(self, spider):
        self.conn.close()
