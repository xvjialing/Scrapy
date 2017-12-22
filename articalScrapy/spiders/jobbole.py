# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse
import datetime

from articalScrapy.items import JobBoleArticleItem,ArticleItemLoader
from articalScrapy.utils.common import get_md5

from scrapy.loader import ItemLoader

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
        # post_urls = response.css("#archive .floated-thumb div.post-thumb a::attr(href)").extract()  # ::attr(href) 获取href属性
        # for post_url in post_urls:
        #     yield Request(url=post_url, callback=self.parse_detail)
        #     # yield Request(url=parse.urljoin(response.url + post_url), callback=self.parse_detail)
        #     print(post_url)

        #增加获取标题图片
        post_nodes=response.css("#archive .floated-thumb div.post-thumb a")
        for post_node in post_nodes:
            img_url= post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            # print(parse.urljoin(response.url,post_url))
            yield Request(url=parse.urljoin(response.url,post_url),callback=self.parse_detail,meta={"front_img_url":img_url})

        #提取下一页url并交给scrapy下载
        next_urls = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_urls:
            # print(next_urls)
            yield Request(url=next_urls, callback=self.parse)

    def parse_detail(self, response):

        article = JobBoleArticleItem()

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
        # front_img_url = response.meta.get("front_img_url","")   # 文章封面图
        # title = response.css(".entry-header h1::text").extract()[0]   # ::text是css伪类选择器
        # create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].replace("·", "").strip()
        # praise_nums =response.css("span.vote-post-up h10::text").extract()[0]
        # re_match= re.match(".*(\d+).*", response.css("span.bookmark-btn::text").extract()[0])
        # if re_match:
        #     fav_nums=int(re_match.group(1))
        # else:
        #     fav_nums = 0
        # re_match = re.match(".*(\d+).*", response.css("a[href='#article-comment'] span::text").extract()[0])
        # if re_match:
        #     comment_nums =re_match.group(1)
        # else:
        #     comment_nums = 0
        # content = response.css("div.entry").extract()[0]
        # tag_list = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tags = ",".join(tag_list)
        #
        # article["title"]=title
        # article["url"]= response.url
        # article["url_object_id"]= get_md5(response.url)
        # try:
        #     create_date=datetime.datetime.strptime(create_date,"%Y%M%D").date()
        # except Exception as e:
        #     create_date =datetime.datetime.now().date()
        # article["create_date"]= create_date
        # article["front_img_url"]= [front_img_url]
        # article["praise_nums"]= praise_nums
        # article["comment_nums"]= comment_nums
        # article["fav_nums"]= fav_nums
        # article["tags"]= tags
        # article["content"]= content

        # 通过item_loader加载item
        item_loader = ArticleItemLoader(item= JobBoleArticleItem(),response= response)
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


        yield article
