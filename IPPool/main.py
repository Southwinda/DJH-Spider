#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:main
   Author:jasonhaven
   date:2018/4/18
-------------------------------------------------
   Change Activity:2018/4/18:
-------------------------------------------------
"""
import IPCrawler
import time

if __name__ == '__main__':
	# url = 'http://www.xicidaili.com/nn/'
	# url_list = IPCrawler.get_url(url, nums=10)
	# for i in url_list:
	# 	print(i)
	# 	content = IPCrawler.get_content(i)
	# 	time.sleep(3)
	# 	IPCrawler.get_info(content)

	with open("daili.txt", "r") as fd:
		datas = fd.readlines()
		for data in datas:
			print(data.split(u":")[0])
			# print('%d : %d'%(out[0],out[1]))
			IPCrawler.verif_ip(data.split(u":")[0].strip(), data.split(u":")[1].strip())
