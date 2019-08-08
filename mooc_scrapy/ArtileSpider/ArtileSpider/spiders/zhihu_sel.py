# coding:utf-8

import scrapy


class ZhihuSpider(scrapy.Spider):
    name = "zhihu_sel"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['https://www.zhihu.com/']

    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhizhu.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    }

    custom_settings = {
        "COOKIES_ENABLED": True
    }

    def start_requests(self):
        from selenium import webdriver
        browser = webdriver.Firefox(executable_path="E:\\geckodriver.exe")

        browser.get("https://www.zhihu.com/signin")
        browser.find_element_by_css_selector(".SignFlow-accountInput.Input-wrapper input").send_keys(
            "18081980605")
        browser.find_element_by_css_selector(".SignFlow-password input").send_keys(
            "Cdgt201301")
        browser.find_element_by_xpath(
            "/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/button").click()
        import time
        time.sleep(10)
        Cookies = browser.get_cookies()
        print(Cookies)
        cookie_dict = {}
        import pickle
        for cookie in Cookies:
            # 写入文件
            #此处大家修改一下自己文件的所在路径
            f = open('E:\\exercise project\\books_exercise_code\\mooc_scrapy\\ArtileSpider\\cookie\\' + cookie['name'] + '.zhihu', 'wb')
            pickle.dump(cookie, f)
            f.close()
            cookie_dict[cookie['name']] = cookie['value']
        # browser.close()
        return [scrapy.Request(url=self.start_urls[0], dont_filter=True, cookies=cookie_dict)]
