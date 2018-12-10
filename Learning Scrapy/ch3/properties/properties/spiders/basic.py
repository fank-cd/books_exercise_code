# -*- coding: utf-8 -*-
import urlparse
from socket import gethostname
from datetime import datetime

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join

from properties.items import PropertiesItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost:9312/properties/property_000000.html']

    def parse(self, response):
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