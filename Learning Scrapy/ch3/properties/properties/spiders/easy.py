# -*- coding: utf-8 -*-

import urlparse
from socket import gethostname
from datetime import datetime


from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join

from properties.items import PropertiesItem


class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost:9312/properties/index_00000.html']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//*[contains(@class,"next")]')),
        Rule(LinkExtractor(restrict_xpaths='//*[@itemprop="url"]'), callback='parse_item')
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i


    def parse_item(self, response):
        """
        @url http://localhost:9312/properties/property_000001.html
        @returns items 1
        @scrapes title price description address image_urls
        @scrapes url project spider server date
        """

        l = ItemLoader(item=PropertiesItem(), response=response)

        l.add_xpath('title', '//*[@itemprop="name"][1]/text()', MapCompose(unicode.strip, unicode.title))
        l.add_xpath('price', './/*[@itemprop="price"][1]/text()', MapCompose(lambda i: i.replace(',', ''), float),
                    re='[,.0-9]+')
        l.add_xpath('description', '//*[@itemprop="description"][1]/text()', MapCompose(unicode.strip), Join())
        l.add_xpath('address', '//*[@itemtype="http://schema.org/Place"][1]/text()', MapCompose(unicode.strip))
        l.add_xpath('image_urls', '//*[@itemprop="image"][1]/@src',
                    MapCompose(lambda i: urlparse.urljoin(response.url, i)))

        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', gethostname())
        l.add_value('date', datetime.now())

        return l.load_item()
