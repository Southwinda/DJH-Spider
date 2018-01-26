# XPath 学习笔记
>http://www.w3school.com.cn/xpath

## 1.XPath 简介
---

>XPath 是一门在 XML 文档中查找信息的语言。XPath 可用来在 XML 文档中对元素和属性进行遍历。
>XPath 是 W3C XSLT 标准的主要元素，并且 XQuery 和 XPointer 都构建于 XPath 表达之上。因此，对 XPath 的理解是很多高级 XML 应用的基础。

#### 1.什么是 XPath?

- XPath 使用路径表达式在 XML 文档中进行导航
- XPath 包含一个标准函数库
- XPath 是 XSLT 中的主要元素
- XPath 是一个 W3C 标准

#### 2.XPath 路径表达式

- XPath 使用路径表达式来选取 XML 文档中的节点或者节点集。这些路径表达式和我们在常规的电脑文件系统中看到的表达式非常相似。

#### 3.XPath 标准函数
- XPath 含有超过 100 个内建的函数。这些函数用于字符串值、数值、日期和时间比较、节点和 QName 处理、序列处理、逻辑值等等。


## 2.XPath 术语
>在 XPath 中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档节点（或称为根节点）。
---

#### 节点（Node）

- 在 XPath 中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档（根）节点。XML 文档是被作为节点树来对待的。树的根被称为文档节点或者根节点。
#### 基本值（或称原子值，Atomic value）

- 基本值是无父或无子的节点。

#### 项目（Item）

- 项目是基本值或者节点。

#### 父（Parent）节点

- 每个元素以及属性都有一个父。

#### 子（Children）

- 元素节点可有零个、一个或多个子。

#### 同胞（Sibling）

- 拥有相同的父的节点

#### 先辈（Ancestor）

- 某节点的父、父的父，等等。

#### 后代（Descendant）

- 某个节点的子，子的子，等等。

## 3.XPath语法

>XPath 使用路径表达式来选取 XML 文档中的节点或节点集。节点是通过沿着路径 (path) 或者步 (steps) 来选取的。

```
<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>
```
#### 选取节点
>XPath 使用路径表达式在 XML 文档中选取节点。节点是通过沿着路径或者 step 来选取的。

![image.png](http://upload-images.jianshu.io/upload_images/8203143-d68073b7705a1169.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

实例:

![image.png](http://upload-images.jianshu.io/upload_images/8203143-d5f8af715a1cbbc9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 谓语（Predicates）
>谓语用来查找某个特定的节点或者包含某个指定的值的节点。谓语被嵌在方括号中。

![image.png](http://upload-images.jianshu.io/upload_images/8203143-a738f13fefe30563.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 选取未知节点
>XPath 通配符可用来选取未知的 XML 元素。

![image.png](http://upload-images.jianshu.io/upload_images/8203143-50a9d4613fb31294.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 选取若干路径
>通过在路径表达式中使用“|”运算符，您可以选取若干个路径。

![image.png](http://upload-images.jianshu.io/upload_images/8203143-733a29d48ab6a40d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 4.XPath轴

![image.png](http://upload-images.jianshu.io/upload_images/8203143-35546cf3a0d71c5e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 位置路径表达式
>位置路径可以是绝对的，也可以是相对的。

- 绝对路径起始于正斜杠( / )，而相对路径不会这样。在两种情况中，位置路径均包括一个或多个步，每个步均被斜杠分割：

- 绝对位置路径：
```
/step/step/...
```
- 相对位置路径：
```
step/step/...
```
- 每个步均根据当前节点集之中的节点来进行计算。

![image.png](http://upload-images.jianshu.io/upload_images/8203143-70efabfe77166ba5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 5.XPath 运算符
>XPath 表达式可返回节点集、字符串、逻辑值以及数字。