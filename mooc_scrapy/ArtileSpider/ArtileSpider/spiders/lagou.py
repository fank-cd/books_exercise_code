# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ArtileSpider.items import LagouJobItem,LagouJobItemLoader

from ArtileSpider.utils.common import get_md5
from datetime import datetime

class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']

    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"
    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhihu.com",
        "User-Agent": agent
    }

    rules = (

        Rule(LinkExtractor(allow=r'zhaopin/.*'), follow=True),
        Rule(LinkExtractor(allow=r'gongsi/j\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),
    )

    def parse_job(self, response):
        # 解析拉勾网的职位
        item_loader = LagouJobItemLoader(item=LagouJobItem(), response=response)
        item_loader.add_xpath("title", ".//div[@class='job-name']/@title")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_xpath("salary", ".//dd[@class='job_request']/p/span[@class='salary']/text()")
        item_loader.add_xpath("job_city", ".//dd[@class='job_request']/p/span[2]/text()")
        item_loader.add_xpath("work_years", ".//dd[@class='job_request']/p/span[3]/text()")
        item_loader.add_xpath("degree_need", ".//dd[@class='job_request']/p/span[4]/text()")
        item_loader.add_xpath("job_type", ".//dd[@class='job_request']/p/span[5]/text()")
        item_loader.add_xpath("tags", ".//ul[@class='position-label clearfix']/li/text()")
        item_loader.add_xpath("publish_time", ".//p[@class='publish_time']/text()")
        item_loader.add_xpath("job_advantage", ".//*[@class='job-advantage']/p/text()")
        item_loader.add_xpath("job_desc", ".//dd[@class='job_bt']/div")
        item_loader.add_xpath("job_addr", ".//div[@class='work_addr']")
        item_loader.add_xpath("company_name", ".//dl[@id='job_company']/dt/a/img/@alt")
        item_loader.add_xpath("company_url", ".//dl[@id='job_company']/dt/a/@href")
        item_loader.add_value("crawl_time", datetime.now())

        job_item = item_loader.load_item()
        return job_item

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i


"""
    def parse_start_url(self, response):
        return []

    def process_results(self, response, results):
        return results

"""
