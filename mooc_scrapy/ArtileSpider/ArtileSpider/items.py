# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
import datetime
import re
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from ArtileSpider.utils.common import extract_nums
from ArtileSpider.settings import SQL_DATE_FORMAT,SQL_DATETIME_FORMAT


from w3lib.html import remove_tags

def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y%m%d").date()
    except:
        create_date = datetime.datetime.now().date()
    return create_date


def get_nums(value):

    match_re = re.match(r".*?(\d+).*", value)
    if match_re:
        nums = match_re.groups(1)
    else:
        nums = 0

    return nums


def remove_comment_tags(value):
    # 去掉tag中多余的评论字段

    if "评论" in value:
        return ""
    else:
        return value


def return_value(value):
    return value


class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class JobBoleAritleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()

    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value),
    )
    front_image_path = scrapy.Field()

    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums),
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums),
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums),
    )

    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(","),
    )
    content = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into jobbole_article(title, url, create_date, fav_nums)
            VALUES (%s, %s, %s, %s)
        """



class ZhihuQUestionItem(scrapy.Item):
    # 知乎的问题item

    zhihu_id = scrapy.Field()
    topics = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    answer_num = scrapy.Field()
    comments_num = scrapy.Field()
    watch_user_num = scrapy.Field()
    click_num = scrapy.Field()
    crawl_time = scrapy.Field()


    def get_insert_sql(self):
        insert_sql = """
            insert into zhihu_question(zhihu_id, topics, url, title,content, answer_num, comments_num,
            watch_user_num, click_num, crawl_time
            
            )
            VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE content=VALUES (content),answer_num=VALUES(answer_num),
            comments_num=VALUES(comments_num),
            watch_user_num=VALUES (watch_user_num),click_num=VALUES (click_num)

        """

        zhihu_id = self["zhihu_id"][0]
        topics = ",".join(self["topics"])
        url = "".join(self["url"])
        title = "".join(self["title"])
        content = "".join(self["zhihu_id"])
        answer_num = extract_nums("".join(self["answer_num"]))
        comments_num = extract_nums("".join(self["comments_num"]))
        watch_user_num = extract_nums("".join(self["watch_user_num"]))
        click_num = extract_nums("".join(self["click_num"]))
        crawl_time = datetime.datetime.now().strftime(SQL_DATETIME_FORMAT)

        params = (zhihu_id, topics, url, title, content, answer_num, comments_num, watch_user_num,
                  click_num, crawl_time)

        return insert_sql, params


class ZhihuAnswerItem(scrapy.Item):
    zhihu_id = scrapy.Field()
    url = scrapy.Field()
    question_id = scrapy.Field()
    author_id = scrapy.Field()
    content = scrapy.Field()
    parise_num = scrapy.Field()
    comments_num = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    crawl_time = scrapy.Field()


    def get_insert_sql(self):
        insert_sql = """
            insert into zhihu_answer(zhihu_id, url, question_id, author_id,content, parise_num, comments_num,
            create_time, update_time, crawl_time
            ) VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE content=VALUES (content),comments_num=VALUES(comments_num),
            parise_num=VALUES(parise_num),update_time=VALUES(update_time)
            
        """


        create_time = datetime.datetime.fromtimestamp(self["create_time"]).strftime(SQL_DATETIME_FORMAT)
        update_time = datetime.datetime.fromtimestamp(self["update_time"]).strftime(SQL_DATETIME_FORMAT)
        params = (
            self["zhihu_id"], self["url"], self["question_id"], self["author_id"], self["content"], self["parise_num"],
            self["comments_num"], create_time, update_time, self["crawl_time"].strftime(SQL_DATETIME_FORMAT)
            )

        return insert_sql,params


def remove_splash(value):
    return value.replace("/", "")


def handle_jobaddr(value):

    addr_list = value.split("\n")
    addr_list = [item.strip() for item in addr_list if not item.strip() == "查看地图"]
    return "".join(addr_list)


class LagouJobItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class LagouJobItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    salary = scrapy.Field()
    job_city = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    work_years = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    degree_need = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    job_type = scrapy.Field()
    publish_time = scrapy.Field()
    job_advantage = scrapy.Field()
    job_desc = scrapy.Field(
        input_processor=MapCompose(remove_tags)
    )
    job_addr = scrapy.Field(
        input_processor=MapCompose(remove_tags, handle_jobaddr),
    )
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    tags = scrapy.Field(
        input_processor=Join(",")
    )
    crawl_time =scrapy.Field()


    def get_insert_sql(self):
        insert_sql ="""
            insert into lagou_job(title, url,url_object_id,salary, job_city, work_years, degree_need, job_type, 
            publish_time, job_advantage, job_desc, job_addr, company_name, company_url, tags, crawl_time)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE salary=VALUES(salary), job_desc=VALUES(job_desc)
        """


        params = (
            self["title"], self["url"], self["url_object_id"], self["salary"], self["job_city"], self["work_years"], self["degree_need"],
            self["job_type"], self["publish_time"], self["job_advantage"], self["job_desc"], self["job_addr"]
            , self["company_name"], self["company_url"], self["tags"], self["crawl_time"].strftime(SQL_DATETIME_FORMAT)
            )

        return insert_sql, params
    
