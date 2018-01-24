#! /usr/bin/env/python
#
# coding utf-8
#
# jasonahven
#
# 
import bs4
from bs4 import BeautifulSoup


def tag(soup):
    '''
    Tag : HTML 标签加上里面包括的内容就是 Tag
    Tag有两个重要的属性，是 name(字符串tag的名字) 和 attrs(字典类型)
    '''
    print('tag()')
    print(soup.title)
    print(soup.a)
    print(soup.p)
    
    print(soup.title.name)
    print(soup.a.name)
    print(soup.p.name)

    print(soup.title.attrs)
    print(soup.a.attrs)
    print(soup.p.attrs)

    print(type(soup.a.attrs))

    #获取attrs的方法，可以修改，删除del
    print(soup.a.attrs['class'])
    print(soup.a['class'])
    print(soup.a.get('class'))


def navigableString(soup):
    '''
    获取标签内部的文字:tag.string即可
    NavigableString  : 就是tag.string的类型
    中文翻译：可遍历字符串
    '''
    print(soup.a.string)#Elsie
    print(type(soup.a.string))#<class 'bs4.element.NavigableString'>
    astring=soup.a.string

def beautifulSoup(soup):
    '''
    BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性
    '''
    print(soup.name)#[document]
    print(soup.attrs)#{}

def comment(soup):
    '''
    Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号
    '''
    print(soup.a)
    print(soup.a.string)#Elsie
    print(type(soup.a.string))#<class 'bs4.element.NavigableString'>
    if type(soup.a.string)==bs4.element.Comment:
        print('comment')



def child(soup):
    '''
    
    1.直接子节点
    .contents : tag 的 .content 属性可以将tag的子节点以列表的方式输出
    .children : 它返回的不是一个 list，不过可以通过遍历获取所有子节点
    
    '''
    print(soup.p.contents)#[<b>The Dormouse's story</b>]

    print(soup.p.children)#<list_iterator object at 0x0000023A44520908>
    
    for child in soup.p.children:
        print(child)


def allchild(soup):
    '''
    
    2.所有子孙节点
    .descendants
    
    .contents 和 .children 属性仅包含tag的直接子节点，
    .descendants 属性可以对所有tag的子孙节点进行递归循环
    和.children类似，我们也需要遍历获取其中的内容

    '''
    for child in soup.body:
        print(child)

def tag_content(soup):
    '''
    3.节点内容
    如果tag有子节点，.string获取子节点
    如果tag没有字标签，则.string返回内容
    '''
    print(soup.p.b)
    print(soup.title.string)

def more_content(soup):
    '''
    4. 多个内容
    .strings : 获取多个内容，不过需要遍历获取
    .stripped_strings : 使用 .stripped_strings 可以去除多余空白内容
    '''
    # for string in soup.strings:
    #     print(repr(string))
    for string in soup.stripped_strings:
        print(string)

def parent(soup):
    '''
    
    5.父节点
    .parent
    .parents

    '''
    p=soup.p
    print(type(p.parent))
    print(p.parent.name)
    print()
    content=soup.title.string
    for parent in content.parents:
        print(parent.name)

def sibling(soup):
    '''
    6.兄弟节点(层次上)
    .next_sibling
    .previous_sibling
    .next_silings
    .previous_siblings
    '''
    p=soup.p
    print(p.next_sibling)
    print(p.next_siblings)
    print(p.previous_sibling)
    print(p.previous_siblings)


def pre_next():
    '''
    7.前后结点
    .next_element
    .next_elements
    
    .previous_element
    .previous_elements
    与 .next_sibling  .previous_sibling 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次
    '''
    html_doc='''<html><head><title>The Dormouse's story</title></head></html>
            '''
    soup=BeautifulSoup(html_doc,'lxml')
    print(soup.head.next_element)
    print(soup.head.previous_element)



if __name__ == '__main__':
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!--this is my comment--></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

    #四种对象结构：Tag , NavigableString , BeautifulSoup , Comment

    soup = BeautifulSoup(html_doc, 'lxml')  # 解析器主要是用有默认的html.parser和lxml，其他的还有
    # print(soup.prettify())  # 标准缩进格式输出

    # *****************************************1.测试四种对象*****************************************
    # tag(soup)
    # navigableString(soup)
    # beautifulSoup(soup)
    # comment(soup)

    # *****************************************2.遍历文档树*****************************************
    # child(soup)
    # allchild(soup)
    # tag_content(soup)
    # more_content(soup)
    # parent(soup)
    # sibling(soup)
    # pre_next()

    # *****************************************3.搜索文档树*****************************************
    
    #find_all( name , attrs , recursive , text , **kwargs )返回list
    #name:tag、正则表达式、字符串、列表、方法，True
    #attr:一个包含属性的字典{'class':'sth'}
    #kwargs:id,class_
    #text:内容匹配，正则、字符串
    #limit:数量限制
    #recursive:是否递归

    #find( name , attrs , recursive , text , **kwargs )返回一个
    #find_parents()  find_parent()
    #find_next_siblings()  find_next_sibling()
    #find_previous_siblings()  find_previous_sibling()
    #find_all_next()  find_next()
    #find_all_previous() 和 find_previous()

    # *****************************************4.CSS选择器*****************************************
    #  soup.select()，返回类型是 list
    # 标签名 soup.select('title')
    # 类名 soup.select('.sister')
    # id soup.select('#link1')
    # 组合 soup.select('p #link1') soup.select('p > link1')
    # 属性查找 soup.select('a[class="sister"]')
