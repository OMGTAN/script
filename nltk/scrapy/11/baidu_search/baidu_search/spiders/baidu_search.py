# coding=utf-8
import sys
import importlib
importlib.reload(sys)

from w3lib.html import remove_tags

import scrapy


class BaiduSearchSpider(scrapy.Spider):
    name = "baidu_search"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://www.baidu.com/s?wd=机器学习"]

    # def parse(self, response):
    #     hrefs = response.selector.xpath(
    #         '//div[contains(@class, "c-container")]/h3/a/@href').extract()
    #     for href in hrefs:
    #         yield scrapy.Request(href, callback=self.parse_url)

    # def parse_url(self, response):
    #     print(remove_tags(response.selector.xpath('//body').extract()[0]))

    def parse(self, response):
        hrefs = response.selector.xpath(
            '//div[contains(@class, "c-container")]/h3/a/@href').extract()
        containers = response.selector.xpath(
            '//div[contains(@class, "c-container")]')
        for container in containers:
            if(len(container.xpath('h3/a/@href').extract()) == 0):
                continue
            href = container.xpath('h3/a/@href').extract()[0]
            title = remove_tags(container.xpath('h3/a').extract()[0])
            c_abstract = container.xpath(
                'div/div/div[contains(@class, "c-abstract")]').extract()
            abstract = ""
            if len(c_abstract) > 0:
                abstract = remove_tags(c_abstract[0])
            request = scrapy.Request(href, callback=self.parse_url)
            request.meta['title'] = title
            request.meta['abstract'] = abstract
            yield request

    def parse_url(self, response):
        print ()
        print ("url:", response.url)
        print ("title:", response.meta['title'])
        print ("abstract:", response.meta['abstract'])
        content = remove_tags(response.selector.xpath('//body').extract()[0])
        print ("content_len:", len(content))
