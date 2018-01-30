# Scrapy 学习进阶
---
#### 1.基本用法
- 目标站点分析
- 抓取第一页
- 获取内容和下一页链接
- 翻页爬取
- 保存结果

> example Quotes

#### 2.项目结构

#### 3.scrapy命令

##### 3.1 global commands

- 创建项目projectname
>scrapy startproject projectname
- 生成爬虫
>scrapy genspider domain
- 交互测试
>scrapy shell url
- 网页浏览
>scrapy view url
- 使用downloader下载url
>scrapy fetch url
##### 3.2 project commands
- 运行spidername
>scrapy crawl spidername
- 测试代码
>scrapy check spidername
- 显示当前项目中全部爬虫
>scrapy list

#### 4.selector
#### 5.spider
#### 6.item pipline
#### 7.downloader
