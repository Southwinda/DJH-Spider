# encoding:utf-8
import time
from http.cookiejar import CookieJar
from urllib import request

import requests
from bs4 import BeautifulSoup
from gevent import monkey
from gevent.pool import Pool

monkey.patch_all()


class SpiderProxy(object):
    def __init__(self):
        self.headers  = [('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'),
                                  ('Host', 'www.xicidaili.com'),
                                  ('Referer', 'http://www.xicidaili.com/n')]

    def get_cookie(self):
        cookie = CookieJar()
        cookie_support = request.HTTPCookieProcessor(cookie)  # cookie处理器
        opener = request.build_opener(cookie_support)
        opener.addheaders = self.headers
        opener.open('http://www.xicidaili.com/')
        return cookie

    def get_all_proxy(self, url, n):
        ''' 取得所有1-n页上的代理IP'''
        data = []
        cookie = self.get_cookie()
        for page in range(1, n):
            if page % 50 == 0:  # 每50页更新下cookie
                cookie = self.get_cookie()

            url = 'http://www.xicidaili.com/nn/%s' % page
            cookie_support = request.HTTPCookieProcessor(cookie)
            opener = request.build_opener(cookie_support)
            request.install_opener(opener)

            req = request.Request(url, headers=dict(self.headers))
            content = request.urlopen(req)
            soup = BeautifulSoup(content, "lxml")
            trs = soup.find('table', id="ip_list").findAll('tr')
            for tr in trs[1:]:
                tds = tr.findAll('td')
                ip = tds[1].text.strip()
                port = tds[2].text.strip()
                protocol = tds[5].text.strip()
                data.append({protocol:'%s://%s:%s\n' % (protocol.lower(), ip, port)})
        return data


class IsActivePorxyIP(object):
    """
     用gevent 异步并发验证 代理IP是不是可以用
    """

    def __init__(self):
        self.proxy = SpiderProxy()
        self.is_active_proxy_ip = []

    def probe_proxy_ip(self, proxy_ip):
        """代理检测"""
        proxy = request.ProxyHandler(proxy_ip)
        opener = request.build_opener(proxy)
        request.install_opener(opener)
        try:
            html = request.urlopen('https://www.baidu.com/')
            # print html.read()
            if html:
                self.is_active_proxy_ip.append(proxy_ip)
                return True
            else:
                return False
        except Exception as e:
            return False


if __name__ == "__main__":
    url = 'http://www.xicidaili.com/wt/'

    p_isactive = IsActivePorxyIP()
    proxy_ip_lst = p_isactive.proxy.get_all_proxy(url, 2)
    print(len(proxy_ip_lst))
    # 异步并发
    pool = Pool(20)
    pool.map(p_isactive.probe_proxy_ip, proxy_ip_lst)
    print(len(p_isactive.is_active_proxy_ip))
