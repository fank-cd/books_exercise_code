# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse

from ArtileSpider.items import JobBoleAritleItem

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        :param response:
        :return:
        """

        # response.xpath("//div[@id='archive']//div[@class='post-thumb']/a/image/@href")
        post_nodes = response.xpath("//div[@id='archive']//div[@class='post-thumb']")
        # 提取文章详情页
        for post_node in post_nodes:
            image_url = post_node.xpath("./a/img/@src").extract_first("")
            post_url = post_node.xpath("./a/@href").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image":image_url}, callback= self.parse_detail)
            # Request(url=post_url, callback=self.parse_detail)
            # print(post_url)

        next_url = response.xpath("//a[@class='next page-numbers']/@href").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        # res_selector = response.xpath('//div[@class="entry-header"]/h1/text()')
        artile_item = JobBoleAritleItem()

        front_image_url = response.meta.get("front_image_url", "")
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first("")
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().\
            replace('·', "").strip()
        praise_nums = response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0]
        fav_nums = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0]
        match_re = re.match(r".*?(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.groups(1)
        else:
            fav_nums = 0
        # pass

        comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_re = re.match(r".*?(\d+).*", comment_nums)
        if match_re:
            comment_nums = match_re.groups(1)
        else:
            comment_nums = 0
        content = response.xpath("//div[@class='entry']").extract()[0]
        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)

        artile_item["title"] = title
        artile_item["url"] = response.url
        artile_item["create_date"] = create_date
        artile_item["front_image_url"] = [front_image_url]
        artile_item["praise_nums"] = praise_nums
        artile_item["comment_nums"] = comment_nums
        artile_item["fav_nums"] = fav_nums
        artile_item["tags"] = tags
        artile_item["content"] = content


        yield artile_item
        # pass
