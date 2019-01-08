# -*- coding: utf-8 -*-
import scrapy
import re
import json
import datetime
from scrapy.loader import ItemLoader
from ArtileSpider.items import ZhihuAnswerItem,ZhihuQUestionItem
from urllib import parse
# python 2
# import urlparse


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    # question的第一页answer的请求url
    start_answer_url = "https://www.zhihu.com/api/v4/questions/{0}/" \
                       "answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed," \
                       "annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit," \
                       "comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings," \
                       "comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt," \
                       "relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled;" \
                       "data[*].mark_infos[*].url;data[*].author.follower_count," \
                       "badge[*].topics&offset={1}&limit={2}&sort_by=default&platform=desktop"

    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"
    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhihu.com",
        "User-Agent": agent
    }

    def parse(self, response):
        # 提取出html页面中的所有URL，并跟踪这些url进一步爬去
        # 如果提取的url格式为 /question/xxx 就下载后直接进入解析函数

        all_urls = response.css("a::attr(href)").extract()
        all_urls = [parse.urljoin(response.url, url) for url in all_urls ]
        all_urls = filter(lambda x: True if x.startwith("https") else False,all_urls)
        for url in all_urls:
            match_obj = re.match("(.*zhihu.com/question/(\d+))(/|$).*", url)
            if match_obj:
                request_url = match_obj.group(1)
                question_id = match_obj.group(2)
                yield scrapy.Request(request_url, headers=self.headers, callback=self.parse_question)
            else:
                # 如果不是question页面则检查该页面中有无url是question页面
                yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse_question(self, response):
        # 处理question页面，从页面中提取出具体的question item

        if "QuestionHeader-title" in response.text:
            # 处理新版本

            match_obj = re.match("(.*zhihu.com/question/(\d+))(/|$).*", response.url)
            if match_obj:
                question_id = int(match_obj.group(2))

            item_loader = ItemLoader(item=ZhihuQUestionItem(), response=response)

            # item_loader.add_css("title", "h1.QuestionHeader-title h2 a::text")
            item_loader.add_xpath("title", "//*[@id='zh-question-title']/h2/a/text()|"
                                           " //*[@id='zh-question-title']/h2/span/text()")
            item_loader.add_css("content", ".QuestionHeader-detail")
            item_loader.add_value("url", response.url)
            item_loader.add_value("zhihu_id", question_id)
            item_loader.add_css("answer_num", ".List-headerText span::text")
            item_loader.add_css("comments_num", "QuestionHeader-actions button:text")
            item_loader.add_css("watch_user_num", ".NumberBoard-value::text")
            item_loader.add_xpath("watch_user_num", "//*[@id='zh-question-side-header-wrap']/text()|"
                                                    "//*[@class='zh-question-followers-sidebar']/div/a/strong/text()")
            item_loader.add_css("topics", ".QuestionHeader-topics .Popover div::text")

            question_item = item_loader.load_item()
            yield scrapy.Request(self.start_answer_url.format(question_id, 0, 20), headers=self.headers, callback=self.parse_answer)
            yield question_item

        else:
            # 处理老版本
            pass

    def parse_answer(self, response):
        #pass
        #处理question的answer
        ans_json = json.load(response.text)
        is_end =  ans_json['paging']["is_end"]
        totals = ans_json['paging']["totals"]
        next_url = ans_json['paging']["next"]

        # pre_url = ans_json['paging']["previous"]
        # 提取answer的具体字段
        for answer in ans_json["data"]:
            answer_item = ZhihuAnswerItem()
            answer_item["zhihu_id"] = answer["id"]
            answer_item["url"] = answer["url"]
            answer_item["question_id"] = answer["question"]["id"]

            answer_item["author_id"] = answer["author"]["id"] if "id" in answer["author"] else None
            answer_item["content"] = answer["content"] if "content" in answer else None

            answer_item["parise_num"] = answer["voteup_count"]
            answer_item["comments_num"] = answer["comment_count"]
            answer_item["create_time"] = answer["created_time"]
            answer_item["update_time"] = answer["updated_time"]

            answer_item["crawl_time"] = datetime.datetime.now()

            yield answer_item

        if not is_end:
            yield scrapy.Request(next_url, headers=self.headers, callback=self.parse_answer)

    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com', callback=self.login, headers=self.headers)]

    def login(self, response):
        response_text = response.text
        match_obj = re.match('.*name="_xsrf" value="(.*?)"', response_text)
        xsrf= ""
        if match_obj:
            xsrf = (match_obj.group(1))
        if xsrf:
            # FormRequest可以完成一个表单提交
            return [scrapy.FormRequest(
                url="https://www.zhihu.com/login/phone_num",
                formdata={
                "_xsrf": xsrf,
                "email": "18684028609",
                "password": "admin",
            },
                headers=self.headers,
                callback=self.check_login

            )]

    def check_login(self,response):
        # 验证服务器的返回数据判断是否成功
        text_json = json.loads(response.text)

        if "msg" in text_json and text_json["msg"] == "登录成功":
            for url in self.start_urls:
                yield scrapy.Request(url, dont_filter=True, headers=self.headers)


