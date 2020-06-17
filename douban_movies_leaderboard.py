#!/usr/bin/env python
# coding: utf-8

# In[122]:


import argparse
from multiprocessing import Pool
import requests
import json
import os
import bs4
import urllib
import time

root_url = 'https://movie.douban.com'
start_url = 'https://movie.douban.com/chart'  # -> 新片榜+分类


# In[94]:


class TypeItem:

    def __init__(self, tname, tid, interval_id):
        self.tname = tname
        self.tid = tid
        self.interval_id = interval_id

    def __str__(self):
        return "{},{},{}".format(self.tname, self.tid, self.interval_id)


# In[95]:


def get_new_film_board_and_categories(start_url):
    new_film_board = []
    type_dict = []
    response = requests.get(start_url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})
    soup = bs4.BeautifulSoup(response.text, 'lxml')

    for t in soup.select_one('div.indent').select('table'):
        item = {}
        item['title'] = t.select_one(
            'div.pl2 a ').get_text().strip().split('/')[0].strip()
        item['link'] = t.select_one('div.pl2 a ').get('href')
        item['abstract'] = t.select_one('div.pl2 p.pl').get_text()
        item['rating'] = t.select_one('div.pl2 span.rating_nums').get_text()
        item['comments'] = t.select_one('div.pl2 span.pl').get_text()[1:-4]
        new_film_board.append(item)

    for s in soup.select('div.aside div.types span'):
        qs = urllib.parse.parse_qs(s.select_one('a').get('href').strip())
        tid = qs['type'][0]
        interval_id = qs['interval_id'][0]
        tname = s.select_one('a').get_text().strip()
        type_dict.append(TypeItem(tname, tid, interval_id))

    return new_film_board, type_dict


# In[135]:


def get_page_urls(type_dict, size=10):
    '''
    size表示获取每个类别的前size名
    '''
    urls = []
    page_size = size // 20 + 1
    for i in range(page_size):
        for item in type_dict:
            url = root_url + '/j/chart/top_list?type={}&interval_id={}&start={}&limit=20'.format(
                item.tid, item.interval_id, i*20)
            urls.append((item.tname, url))
    return urls


# In[169]:


def get_data(url):
    tname = url[0]
    link = url[1]
    response = requests.get(link,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})
    data = json.loads(response.text)
    return tname, data


def save_data(tname, data):
    if not os.path.exists('./results'):
        os.mkdir('./results')
    json.dump(data, open('./results/'+str(tname)+'.json',
                         'w', encoding='utf-8'), ensure_ascii=False)
    print('save at ./results/'+tname+'.json')


# In[164]:


def parse_args():
    parser = argparse.ArgumentParser(description='采集豆瓣电影排行榜')
    parser.add_argument('--size', metavar='SIZE', type=int,
                        default=10, help='show the top size entries only.')
    parser.add_argument('--workers', type=int, default=4,
                        help='number of workers to use, 4 by default.')
    return parser.parse_args()


# In[171]:


def multi_process(options):
    if options.workers is None or options.workers <= 0:
        options.workers = 4
    if options.size is None or options.size <= 0:
        options.size = 10
    pool = Pool(options.workers)
    new_film_board, type_dict = get_new_film_board_and_categories(start_url)
    urls = get_page_urls(type_dict, size=options.size)
    results = pool.map(get_data, urls)

    if not os.path.exists('./results'):
        os.mkdir('./results')
    save_data('new_film_board', new_film_board)
    for tname, data in results:
        save_data(tname, data)


if __name__ == '__main__':
    multi_process(parse_args())
