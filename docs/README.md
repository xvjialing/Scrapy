# Scrapy

## 正则表达式

| 字符              |                    作用                    |
| --------------- | :--------------------------------------: |
| ^               |                 匹配字符串的开头                 |
| $               |                匹配字符串的末尾。                 |
| .               | 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。 |
| [...]           |    用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'    |
| [^...]          |     不在[]中的字符: \[^abc]匹配除了a,b,c之外的字符。     |
| re*             |               匹配0个或多个的表达式。               |
| re+             |            匹配1个或多个的表达式（至少一个）。            |
| re?             |    匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式（从左往右）     |
| re{ n}          |               精确匹配n个前面的表达式               |
| re{ n, m}       |              匹配大于等于n个前面表达式               |
| re{ n, m}       |  匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式（从右往左匹配）   |
| a\| b           |                  匹配a或b                   |
| \s              |        匹配任意空白字符 ，等价于 [\t\n\r\f].         |
| \S              |                 匹配任意非空字符                 |
| \w              |                  匹配字母数字                  |
| \W              |                 匹配非字母数字                  |
| [\u4E00-\u9FA5] |                  匹配任意汉字                  |
| \d              |            匹配任意数字，等价于 [0-9].             |
| \D              |                 匹配任意非数字                  |

## 网站树结构

![网站结构](http://p1i22rxiz.bkt.clouddn.com/tree.jpg)

* 深度优先算法

深度优先算法的遍历顺序是A-B-D-E-I-C-F-G-H(递归实现)

* 广度优先算法

广度优先算法的遍历顺序是A-B-C-D-E-F-G-H-I(队列实现)

## 爬虫去重策略

1. 将访问过的url保存如数据库
2. 将访问过的url存入set中，只需要o(1)的代价就可以查询url。100000000\*2byte\*50个字符/1024/1024/1024=9G
3. url经过md5等方法哈希后保存入set中
4. 用bitmap方法，将访问过的url通过hash函数映射到某一位
5. bloomfilter方法对bitmap进行改进，多重hash函数降低冲突

## 字符串编码

1. 计算机只能处理数字，文本转换为数字才能处理。计算机中8个bit作为一个字节，所以一个字节能表示的最大数字是255。
2. 计算机是美国人发明的，一个字节就能表示所有字符了，所以ASCII(一个字节)编码就成为美国人的标准编码。
3. 但ASCII处理中文明显是不够的，中文不止255个汉字，所以制定了GB2312，用两个字节表示一个汉字。但不同国家发展的编码不同，标准不统一。
4. Unicode将所有的语言统一到一套编码中。但中英文都用Unicode浪费空间，所以出现了可变长的的编码"UTF-8",把英文变成一个字节，汉字变成3个字节，生僻字变成4-6个字节。



## 初始化工程

```
scrapy startproject articalScrapy
```

初始化的工程中，spiders文件夹用于存放爬虫文件，items.py用于定义数据保存的格式，middlewares用于保存中间件，pipeline.py用于数据存储操作，setting.py用于系统设置。

*创建爬虫模版*

```
scrapy genspider example example.com
```

运行单个爬虫

```
scrapy crawl jobbole
```

## xpath简介

1. xpath使用路径表达式在xml和html中进行导航
2. xpath包含标准函数库
3. xpath是一个w3c的标准

### xpath节点关系

1. 父节点，相邻上一层级的节点
2. 子节点，相邻下一层级节点
3. 同胞节点，同一层级的节点
4. 先辈节点，该节点所在层级之上的节点
5. 后代节点，该节点所在层级之下的节点

### xpath语法

| 表达式                     | 说明                                       |
| ----------------------- | ---------------------------------------- |
| article                 | 选取所有article元素                            |
| /article                | 选取根元素article                             |
| Article/a               | 选取所有属于article的子元素的a元素                    |
| //div                   | 选取所有div子元素                               |
| Article//div            | 选取所有属于article元素的后代的div元素，不管它出现在article之下的任何位置 |
| //@class                | 选取所有名为class的属性                           |
| /article/div[1]         | 选取属于article子元素的第一个div元素                  |
| /article/div[last()]    | 选取属于article子元素的最后一个div元素                 |
| /article/div[last()-1]  | 选取属于article子元素的倒数第二个div元素                |
| //div[@lang]            | 选取所有拥有lang属性的div元素                       |
| //div[@lang='eng']      | 选取所有lang属性为eng的div元素                     |
| /div/*                  | 选取属于div元素的所有子节点                          |
| //*                     | 选取所有元素                                   |
| //div[@*]               | 选取所有带属性的div元素                            |
| /div/a \| //div/p       | 选取所有div元素的a和p元素                          |
| //span \| //ul          | 选取文档中的span元素与ul元素                        |
| article/div/p \| //span | 选取所有属于article元素的div元素的p元素以及文档中的所有的span元素 |
| ::text()                | text伪类，用于获取值，例如a::text()                 |

### scrapy shell调试

在终端程序中使用shell命令调试

```Shell
scrapy shell http://blog.jobbole.com/112809/
```

 结果是：

```shell
2017-12-15 13:54:56 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
2017-12-15 13:54:56 [scrapy.core.engine] INFO: Spider opened
2017-12-15 13:54:56 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://blog.jobbole.com/112809/> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x103f4d080>
[s]   item       {}
[s]   request    <GET http://blog.jobbole.com/112809/>
[s]   response   <200 http://blog.jobbole.com/112809/>
[s]   settings   <scrapy.settings.Settings object at 0x104d4d8d0>
[s]   spider     <JobboleSpider 'jobbole' at 0x10605dc88>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects 
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
```

使用"response"命令调试

```shell
>>> titile = response.xpath('//div[@class="entry-header"]/h1/text()')
>>> titile
[<Selector xpath='//div[@class="entry-header"]/h1/text()' data='谈谈程序员的离职和跳槽'>]
```

获取具体值：

```shell
>>> titile.extract()
['谈谈程序员的离职和跳槽']
>>> titile.extract()[0]
'谈谈程序员的离职和跳槽'
```

extract()函数获取到的值是数组，取第一个值就能得到具体值。

```shell
>>> titile.xpath("//*")
[]
>>> titile
[<Selector xpath='//div[@class="entry-header"]/h1/text()' data='谈谈程序员的离职和跳槽'>]
```

在调用xpath方法得到的值还可以继续使用xpath，但一旦使用extract()得到具体值后就无法再使用xpath()函数。

获取网页上的文章日期：

```shell
>>> text = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].replace("·","").strip()
>>> text
'2017/12/09'
```

在获取到的某个节点的extract()后，得到的值会忽略这个节点内部的节点，replace()函数用于替换字符，strip()函数用来除去换行符。

获取点赞数：

网页源代码：

```html
<span data-post-id="112809" class=" btn-bluet-bigger href-style vote-post-up   register-user-only "><i class="fa  fa-thumbs-o-up"></i> <h10 id="112809votetotal">1</h10> 赞</span>
```

shell命令：

```shell
>>> star = response.xpath("//span[@class='vote-post-up']")
>>> star
[]
```

因为class中不止一个，单取"vote-post-up"是不对的，所以取到的值是空的。

```shell
>>> star = response.xpath("//span[contains(@class,'vote-post-up')]")
>>> star
[<Selector xpath="//span[contains(@class,'vote-post-up')]" data='<span data-post-id="112809" class=" btn-'>]
>>> star = response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0]
>>> star
'1'
```

这时应该使用contains函数，这样就能取到了。

获取收藏数：

```shell
>>> prase_nums = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0]
>>> prase_nums
' 5 收藏'
>>> import re
>>> prase_nums = re.match(".*(\d+).*", prase_nums).group(1)
>>> prase_nums
'5'
```

获取到的值通过正则表达式进行过滤。

获取评论数：

```shell
>>> fav_nums = re.match(".*(\d+).*", response.xpath("//*[@id='post-112809']/div[3]/div[3]/a/span/text()").extract()[0]).group(1)
>>> fav_nums
'5'
```

## css选择器

| 表达式                            | 说明                                 |
| ------------------------------ | ---------------------------------- |
| *                              | 选择所有节点                             |
| \#container                    | 选择id为container的节点                  |
| .container                     | 选择所有class包含container的节点            |
| li a                           | 选择所有li下的所有a节点                      |
| ul + p                         | 选择ul后面的第一个p元素                      |
| div#container > ul             | 选择id为container的div的第一个ul子元素        |
| ul ~ p                         | 选取与ul相邻的所有p元素                      |
| a[title]                       | 选取所有有title属性的a元素                   |
| a\[href="http://jobbole.com"\] | 选取所有href属性为http://jobbole.com值的a元素 |
| a[href*="jobbole"]             | 选取所有href属性包含jobbole的a元素            |
| a[href^="http"]                | 选取所有href属性值以http开头的a元素             |
| a[href$=".jpg"]                | 选取所有href属性值以.jpg结尾的a元素             |
| input[type=radio]:checked      | 选择选中的radio的元素                      |
| div:not(#container)            | 选取所有id非container的div元素             |
| Li:nth-child(3)                | 选取第三个li元素                          |
| R:nth-child(2n)                | 第偶数个tr                             |
| ::text                         | 用于获取值                              |
| ::attr(属性名)                    | 用于获取属性的值，例如::attr(href)            |

css选择器获取标题

```Shell
>>> response.css(".entry-header h1::text").extract()[0]
'谈谈程序员的离职和跳槽'
```

获取日期

```Shell
>>> response.css("p.entry-meta-hide-on-mobile::text").extract()[0].replace("·","").strip()
'2017/12/09'
```

获取点赞数：

```Shell
>>> response.css("span.vote-post-up h10::text").extract()[0]
'1'
```

获取收藏数：

```shell
>>> re.match(".*(\d+).*",response.css("span.bookmark-btn::text").extract()[0]).group(1)
'5'
```

评论数：

```shell
>>> re.match(".*(\d+).*",response.css("a[href='#article-comment']::text").extract()[0]).group(1)
'6'
```

***

### 编写爬虫

获取页面url

```python
post_urls = response.css(".floated-thumb div a::attr(href)").extract()  # ::attr(href) 获取href属性
```

结果：

```shell
http://blog.jobbole.com/113339/
http://blog.jobbole.com/112148/
http://blog.jobbole.com/113333/
http://blog.jobbole.com/113328/
http://blog.jobbole.com/113230/
http://blog.jobbole.com/113315/
http://blog.jobbole.com/113312/
```

爬虫示例：

```python
# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        1. 获取文章列表页中的文章url进行解析，并交给scrapy下载后进行解析
        2. 获取下一页的url并交给scrapy进行下载，下载完成交给parse函数
        :param response:
        :return:
        """

        # 解析列表页中的所有文章url，并交给scrapy下载后进行解析
        post_urls = response.css("#archive .floated-thumb div.post-thumb a::attr(href)").extract()  # ::attr(href) 获取href属性
        for post_url in post_urls:
            yield Request(url=post_url, callback=self.parse_detail)
            # yield Request(url=parse.urljoin(response.url + post_url), callback=self.parse_detail)
            print(post_url)

        #提取下一页url并交给scrapy下载
        next_urls = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_urls:
            print(next_urls)
            yield Request(url=next_urls, callback=self.parse)

    def parse_detail(self, response):
        # 提取文章具体字段

        # xpath选择器
        # title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0] # extract()函数获取到具体值，由于获取到的是数组，所以取第一个值
        # create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].replace("·", "").strip()   # replace()函数用于替换字符，strip()函数用于去除换行符等
        # star = response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0] # 当class属性中有多个属性值时，使用contains(）函数
        # re_match= re.match(".*(\d+).*", response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0])
        # if re_match:
        #     prase_nums = re_match.group(1)
        # else:
        #     prase_nums = 0
        # fav_nums = re.match(".*(\d+).*", response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]).group(1)
        # content = response.xpath("//div[@class='entry']").extract()[0]
        # tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tags = ",".join(tag_list)

        #css 选择器
        title2 = response.css(".entry-header h1::text").extract()[0]   # ::text是css伪类选择器
        create_date2 = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].replace("·", "").strip()
        star2 =response.css("span.vote-post-up h10::text").extract()[0]
        pre_bookmark=response.css("span.bookmark-btn::text").extract()[0]
        re_match= re.match(".*(\d+).*", pre_bookmark)
        if re_match:
            prase_nums2=re_match.group(1)
        else:
            prase_nums2 = 0
        pre_comment_nums=response.css("a[href='#article-comment'] span::text").extract()[0]
        re_match = re.match(".*(\d+).*", pre_comment_nums)
        if re_match:
            fav_nums2 =re_match.group(1)
        else:
            fav_nums2 = 0
        content2 = response.css("div.entry").extract()[0]
        tag_list2 = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        tag_list2 = [element for element in tag_list2 if not element.strip().endswith("评论")]
        tags2 = ",".join(tag_list2)
        pass
```

***

## 数据结构定义与图片下载存储

在items.py文件中定义item:

```python
class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    praise_nums = scrapy.Field()
    fav_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
```

修改爬虫，加入标题图片链接：

```python
#增加获取标题图片
post_nodes=response.css("#archive .floated-thumb div.post-thumb a")
for post_node in post_nodes:
    img_url= post_node.css("img::attr(src)").extract_first("")
    post_url = post_node.css("::attr(href)").extract_first("")
    print(parse.urljoin(response.url,post_url))
    yield Request(url=parse.urljoin(response.url,post_url),callback=self.parse_detail,meta={"front_img_url":img_url})
```

在爬虫中加入item：

```python
from articalScrapy.items import JobBoleArticleItem  # 导入item

def parse_detail(self, response):
    article = JobBoleArticleItem()  # 实例化item
	…………
    
    article["title"]=title
    article["url"]= response.url
    article["create_date"]= create_date
    article["front_img_url"]= front_img_url
    article["praise_nums"]= praise_nums
    article["comment_nums"]= comment_nums
    article["fav_nums"]= fav_nums
    article["tags"]= tags
    article["content"]= content

    yield article

```

开启图片下载：

在setting.py文件中：

```python
ITEM_PIPELINES = {   #此处代码本来就用，只需要解除注释
   'articalScrapy.pipelines.ArticalscrapyPipeline': 300,
   'scrapy.pipelines.images.ImagesPipeline': 1, # 设置image的pipeline,数字越小优先级越高
}
IMAGES_URLS_FIELD = "front_img_url"  #设置图片的参数
project_dir=os.path.abspath(os.path.dirname(__file__)) #获取父路径
IMAGES_STORE = os.path.join(project_dir,"imgs") #设置最终的图片存储路径
```

此时运行还是会报错：

```shell
  File "/Users/xvjialing/python-virtualenv/articalScrapy/lib/python3.6/site-packages/scrapy/pipelines/images.py", line 15, in <module>
    from PIL import Image
ModuleNotFoundError: No module named 'PIL'
```

显示缺少模块：

```shell
$ pip install pillow
Collecting pillow
  Downloading Pillow-4.3.0-cp36-cp36m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (3.5MB)
    100% |████████████████████████████████| 3.6MB 132kB/s 
Collecting olefile (from pillow)
  Downloading olefile-0.44.zip (74kB)
    100% |████████████████████████████████| 81kB 194kB/s 
Building wheels for collected packages: olefile
  Running setup.py bdist_wheel for olefile ... done
  Stored in directory: Caches/pip/wheels/20/58/49/cc7bd00345397059149a10b0259ef38b867935ea2ecff99a9b
Successfully built olefile
Installing collected packages: olefile, pillow
Successfully installed olefile-0.44 pillow-4.3.0
```

此时运行还是会报错：

```shell
raise ValueError('Missing scheme in request url: %s' % self._url)
```

因为此时需要的值url为数组：

```python
article["front_img_url"]= front_img_url
改为
article["front_img_url"]= [front_img_url]
```

在pipeline.py中自定义图片路径存储pipeline：

```python
from scrapy.pipelines.images import ImagesPipeline  #继承ImagePipeline
class  ArticleImagePipeline(ImagesPipeline):   #继承ImagePipeline
    def item_completed(self, results, item, info):
        for ok,value in results:
            image_file_path = value['path']   # 取出图片存储路径
            item['front_img_path']=image_file_path  #将图片存储路径存入item中
        return item
```

在setting.py中使用自定义的pipeline:

```python
ITEM_PIPELINES = {     #此处代码本来就用，只需要解除注释
   'articalScrapy.pipelines.ArticalscrapyPipeline': 300,
   'articalScrapy.pipelines.ArticleImagePipeline': 2,
   # 'scrapy.pipelines.images.ImagesPipeline': 1,   # 设置image的pipeline,数字越小优先级越高
}
```

***

## 将数据保存到json文件中

定义json的pipeline

```python
import codecs
import json
from scrapy.exporters import JsonItemExporter

class JsonEncodingPipeline(object):
    #自定义json文件的导出
    def __init__(self):
        self.file= codecs.open('article.json','w',encoding="utf-8")  # 'w'是write的意思
    def process_item(self, item, spider):
        lines= json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(lines)
        return item
    def spider_closed(self, spider):
        self.file.close()

class JsonExporterPipeline(object):
    #调用scrapy提供的json exporter导出json文件
    def __init__(self):
        self.file= open("articleexporter.json","wb")  # "wb"的意思是以二进制的形式打开
        self.exporter =JsonItemExporter(self.file,encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
```

***

## 保存数据到mysql数据库

安装mysql驱动:

```shell
pip install mysqlclient
```

mac系统此时需要安装一个软件

```shell
xcode-select --install
```

*同步写入mysql*

```python
class MysqlPipeline(object):
    #采用同步的机制写入mysql
    def __init__(self):
        self.conn= MySQLdb.connect("121.196.194.14","root","lytech","articlespider", 3336, charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql="""
            insert into article(title,url,create_date,fav_nums)
            VALUES (%s,%s,%s,%s)
        """
        self.cursor.execute(insert_sql,(item["title"],item["url"],item["create_date"],item["fav_nums"]))
        self.conn.commit()
        return item
```

上面的不同使用mysql的方式会在数据量大的时候造成阻塞。下面用twisted提供的mysql连接池实现mysql异步操作。

先在setting.py中加入mysql的配置	

```python
MYSQL_HOST = "121.196.194.14"
MYSQL_DBNAME = "articlespider"
MYSQL_USER = "root"
MYSQL_PASSWORD = "lytech"
MYSQL_PORT = 3336
```

编写异步插入爬虫：

```python
from twisted.enterprise import adbapi

import MySQLdb
import MySQLdb.cursors

class MysqlTwistedPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):  # 读入setting.py文件中的mysql配置
        dbparams=dict(host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            port = settings["MYSQL_PORT"],
            charset='utf8',
            cursorclass =MySQLdb.cursors.DictCursor,
             use_unicode=True)

        dbpool= adbapi.ConnectionPool("MySQLdb", **dbparams)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步
        query= self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_error)  # 处理异常

    def handle_error(self,failure):
        # 处理异步插入的错误
        print(failure)

    def do_insert(self,cursor,item):
        # 执行具体插入
        insert_sql = """
                    insert into article(title,url,create_date,fav_nums,comment_nums,praise_nums,tag,content,front_img_url,url_object_id)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
        cursor.execute(insert_sql, (item["title"], item["url"], item["create_date"],item["fav_nums"],item["comment_nums"],
                                    item["praise_nums"],item["tags"],item["content"],item["front_img_url"],item["url_object_id"]))
```

这样，将爬取的数据存入mysql就实现了。

***

## ItemLoder

> Item Loaders提供了一种便捷的方式填充抓取到的 Items 。 虽然Items可以使用自带的类字典形式API填充，但是Items Loaders提供了更便捷的API， 可以分析原始数据并对Item进行赋值。

在爬虫中：初始化ItemLoader

```python
from scrapy.loader import ItemLoader

# 通过item_loader加载item
        item_loader = ItemLoader(item= JobBoleArticleItem(),response= response)
        # item_loader.add_xpath()  #与add_css()一样
        item_loader.add_value("front_img_url",[response.meta.get("front_img_url","")])  #将通过css样式匹配的值赋给"title"
        item_loader.add_css("title",".entry-header h1::text")
        item_loader.add_css("create_date","p.entry-meta-hide-on-mobile::text")
        item_loader.add_css("praise_nums","span.vote-post-up h10::text")
        item_loader.add_css("fav_nums","span.bookmark-btn::text")
        item_loader.add_css("comment_nums","a[href='#article-comment'] span::text")
        item_loader.add_css("content","div.entry")
        item_loader.add_css("tags","p.entry-meta-hide-on-mobile a::text")
        item_loader.add_css("content","div.entry")
        item_loader.add_css("content","div.entry")
        item_loader.add_css("content","div.entry")
        item_loader.add_value("url",response.url)  #直接将值赋给"url"
        item_loader.add_value("url_object_id",get_md5(response.url))

        article = item_loader.load_item()
```

在items.py中对item加入处理逻辑：

```python
from scrapy.loader.processors import MapCompose, TakeFirst

def add_jobbole(value):
    return value+"-jobbole"


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y%M%D").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()

    return create_date

class JobBoleArticleItem(scrapy.Item):
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_img_url = scrapy.Field()
    front_img_path = scrapy.Field()
    title = scrapy.Field(
        input_processor =MapCompose(add_jobbole) # 值的预处理
    )
    create_date = scrapy.Field(
        input_processor = MapCompose(date_convert),
        output_processor = TakeFirst()  # 返回的值取list的第一个值
    )
    praise_nums = scrapy.Field()
    fav_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
```

这样取到的值就是经过input_processor与output_processor处理的。

但为每个值都设置一个`output_processor = TakeFirst()`太麻烦，所以这里需要自定义一个ItemLoader

items.py:

```python
from scrapy.loader import ItemLoader

class ArticleItemLoader(ItemLoader):
    # 自定义ItemLoader
    default_output_processor = TakeFirst()
```

并在jobble.py中将默认的ItemLoader替换：

```python
from articalScrapy.items import ArticleItemLoader

item_loader = ItemLoader(item= JobBoleArticleItem(),response= response)
改为
item_loader = ArticleItemLoader(item= JobBoleArticleItem(),response= response)
```

最终items.py:

```python
import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst,Join
from scrapy.loader import ItemLoader
import datetime
import re


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y%M%D").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()

    return create_date

def nums_convert(value):
    re_match = re.match(".*(\d+).*", value)
    if re_match:
        nums = int(re_match.group(1))
    else:
        nums = 0
    return nums

def tags_convert(value):
    if "评论" in value:
        return ""
    else:
        return value

def return_value(value):
    return value

class ArticleItemLoader(ItemLoader):
    # 自定义ItemLoader
    default_output_processor = TakeFirst()


class JobBoleArticleItem(scrapy.Item):
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_img_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    front_img_path = scrapy.Field()
    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor = MapCompose(date_convert)
    )
    praise_nums = scrapy.Field(
        input_processor=MapCompose(nums_convert)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(nums_convert)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(nums_convert)
    )
    content = scrapy.Field()
    tags = scrapy.Field(
        input_processor=MapCompose(tags_convert),
        output_processor=Join(",")
    )
```

***

常见Http状态码：

| code    | 说明            |
| ------- | ------------- |
| 200     | 请求被成功处理       |
| 301/302 | 永久性重定向/临时性重定向 |
| 403     | 没有权限访问        |
| 404     | 表示没有对应的资源     |
| 500     | 服务器错误         |
| 503     | 服务器停机或正在维护    |

接下来开始爬取知乎

首先分析知乎的登陆方法，这里使用Firefox进行分析，根据手机与邮箱会有两个不同的登陆连接：`手机号：https://www.zhihu.com/login/phone_num`与`邮箱：https://www.zhihu.com/login/email`

手机号登陆：

![手机号登陆](http://p1i22rxiz.bkt.clouddn.com/phone_login.jpg)

邮箱登陆：

![邮箱登陆](http://p1i22rxiz.bkt.clouddn.com/email_login.jpg)

而_xsrf就在登陆页的网页源代码中：

```html
<input type="hidden" name="_xsrf" value="35626566356431662d343830322d346564352d613230632d613232366530353466343033"/>
```

安装requests：

```shell
pip install requests
```

在utils文件夹中创建zhihu_login_requests.py:

