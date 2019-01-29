# coding:utf-8
from scrapy_redis.spiders import RedisSpider
import datetime
import scrapy
import re
from scrapy.http import Request
from urllib import parse
from scrapy.loader import ItemLoader


from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class JobboleSpider(RedisSpider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']

    start_urls = ['http://blog.jobbole.com/all-posts/']
    redis_key = "jobbole:start_urls"

    def parse(self, response):
        # do stuff
        if response.status == 404:
            self.fail_urls.append(response.url)
            self.crawler.stats.inc_value("failed_url")

        # response.xpath("//div[@id='archive']//div[@class='post-thumb']/a/image/@href")
        post_nodes = response.xpath("//div[@id='archive']//div[@class='post-thumb']")
        # 提取文章详情页
        for post_node in post_nodes:
            image_url = post_node.xpath("./a/img/@src").extract_first("")
            post_url = post_node.xpath("./a/@href").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url),
                          meta={"front_image": image_url}, callback=self.parse_detail, dont_filter=True)
            # Request(url=post_url, callback=self.parse_detail)
            # print(post_url)

        next_url = response.xpath("//a[@class='next page-numbers']/@href").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        pass