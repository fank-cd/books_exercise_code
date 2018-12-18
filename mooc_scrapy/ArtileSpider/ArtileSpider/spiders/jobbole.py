# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114549/']

    def parse(self, response):
        res_selector = response.xpath('//div[@class="entry-header"]/h1/text()')
        pass
