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
