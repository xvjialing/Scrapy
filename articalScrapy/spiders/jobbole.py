# -*- coding: utf-8 -*-
import scrapy
import re


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112809/']

    def parse(self, response):

        # re_selector=response.xpath("/html/body/div[3]/div[3]/div[1]/div[1]/h1")   # 源码中的结构与实际显示页面可能不同，有的html代码是通过js动态生成的，所以有的需要查看源码而不是检查
        # re_selector=response.xpath('//*[@id="post-112809"]/div[1]/h1/text()')    # text()函数取的是当前结构的值
        # re_selector=response.xpath('//div[@class="entry-header"]/h1/text()')    # text()函数取的是当前结构的值

        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0] # extract()函数获取到具体值，由于获取到的是数组，所以取第一个值

        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].replace("·", "").strip()   # replace()函数用于替换字符，strip()函数用于去除换行符等

        star = response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0] # 当class属性中有多个属性值时，使用contains(）函数

        prase_nums = re.match(".*(\d+).*", response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0]).group(1) # 利用re.match()对取到的值进行过滤

        fav_nums = re.match(".*(\d+).*", response.xpath("//*[@id='post-112809']/div[3]/div[3]/a/span/text()").extract()[0]).group(1)

        content = response.xpath("//div[@class='entry']").extract()[0]

        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)
        pass
