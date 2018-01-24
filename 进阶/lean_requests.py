#! /usr/bin/env/python
#
# coding utf-8
#
# jasonahven
#

import requests


def base():
    '''
    requets 基本使用
    '''
    url = 'http://httpbin.org'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    }
    response = requests.get(url + '/' + 'get',headers=headers)
    print(response.status_code)
    print(response.cookies)
    print(response.encoding)
    print(response.apparent_encoding)
    print(response.content)
    print(response.text)

    # response = requests.post(url + '/' + 'post')
    # print(response.status_code)

    # response = requests.put(url + '/' + 'put')
    # print(response.status_code)

    # response = requests.delete(url + '/' + 'delete')
    # print(response.status_code)

    # response = requests.head(url + '/' + 'get')
    # print(response.status_code)

    # response = requests.options(url + '/' + 'get')
    # print(response.status_code)

def get():
    '''
    requets get
    '''
    url = 'http://httpbin.org'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    }
    parameters={"a":'aa','b':'bb'}

    response = requests.get(url + '/' + 'get',headers=headers ,params=parameters)
    print(response.url)#http://httpbin.org?a=aa&b=bb
    print(response.request)
    print(response.json())


def post():
    '''
    requets post
    '''
    url = 'http://httpbin.org'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    }
    form={"a":'aa','b':'bb'}

    # response = requests.post(url + '/' + 'post',headers=headers ,data=form)
    # print(response.url)#http://httpbin.org/post
    # print(response.request)
    # print(response.json())

    import json
    load_data={"d1":'aa','d2':'bb'}
    response = requests.post(url + '/' + 'post',headers=headers ,data=json.dumps(load_data))
    print(response.request)
    print(response.json())


def cookie():
    '''
    测试cookie的设置与访问
    '''
    #发送请求中cookies
    cookies=dict(abc='ABC')
    url = 'http://httpbin.org/get'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    }
    response=requests.get(url,cookies=cookies)
    print(response.text)

    #输出响应中的cookies
    print(response.cookies)
    #print(response.cookies['name'])

def timeout():
    '''
    设置最大请求时间
    '''
    url = 'http://httpbin.org/get'
    response=requests.get(url,timeout=0.01)


def session():
    '''
    会话
    '''
    #每一次请求都相当于发送一个新的请求，即使是同一个网址
    url='http://httpbin.org/cookies/set/sessioncookie/123456789'
    requests.get(url)
    resp=requests.get('http://httpbin.org/cookies')
    print(resp.json())#{'cookies':'{}'}

    #一次会话
    s=requests.Session()
    s.get(url)#设置cookies
    resp=s.get('http://httpbin.org/cookies')#获取cookies
    print(resp.json())#{'cookies': {'sessioncookie': '123456789'}}

def proxy():
    '''
    使用代理:配置单个请求方式和全局配置方式
    '''
    proxies={
        'https':'http://41.118.132.69:4433'
    }
    #配置单个请求方式
    resp=requests.post('http://httpbin.org/post',proxies=proxies)
    print(resp.json())


def SSL():
    '''
    SSL证书验证,verify=False,True
    '''
    resp=requests.get('https://kyfw.12306.cn/otn/',verify=True)
    # print(resp.text)

    resp=requests.get('https://github.com',verify=True)
    print(resp.text)

if __name__ == '__main__':
    SSL()

