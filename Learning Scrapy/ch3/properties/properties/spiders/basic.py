# -*- coding: utf-8 -*-
import scrapy
from properties.items import PropertiesItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://localhost:9312/properties/property_000000.html']

    def parse(self, response):

        """
        self.log("title:%s" % response.xpath(
            '//*[@itemprop="name"]/text()'
        ).extract())
        self.log("price:%s" % response.xpath(
            '//*[@itemprop="price"]/text()'
        ).re('[.0-9]+'))
        self.log("description: %s" % response.xpath(
            '//*[@itemprop="description"]/text()'
        ).extract())
        self.log("address: %s" % response.xpath(
            '//*[@itemtype="http://schema.org/Place"]/text()'
        ).extract())
        self.log("image_urls: %s " % response.xpath(
            '//*[@itemprop="image"]/@src'
        ).extract())
        """
        item = PropertiesItem()
        item['title'] = response.xpath('//*[@itemprop="name"]/text()').extract()
        item['price'] = response.xpath('//*[@itemprop="price"]/text()').re('[.0-9]+')
        item['description'] = response.xpath('//*[@itemprop="description"]/text()').extract()
        item['address'] = response.xpath('//*[@itemtype="http://schema.org/Place"]/text()').extract()
        item['image_urls'] = response.xpath('//*[@itemprop="image"]/@src').extract()
        return item