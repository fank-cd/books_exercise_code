# coding:utf-8

from selenium import webdriver
from time import sleep
from scrapy.selector import Selector




# browser.find_element_by_xpath().send_keys()
#browser.quit()
# # selenium完成微博模拟登录
# browser.get("https://weibo.com/login.php")
# # t_selector = Selector(text=browser.page_source)
# # t_selector.xpath("")
#
# print(browser.page_source)
# sleep(10)
# #browser.find_element_by_id("loginname").send_keys("18684028609")
#
#
#
# browser.find_element_by_xpath(".//input[@id='loginname']").send_keys("18684028609")
# browser.find_element_by_xpath(".//div[@class='info_list password']/div/input[@class='W_input']").send_keys("Cdkc201301")
# browser.find_element_by_xpath(".//div[@class='info_list login_btn']/a[@node-type='submitBtn']").click()
# sleep(5)
# for i in range(3):
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage")
#     sleep(3)

# 设置不加载图片


# 设置不加载图片


# firefox_profile = webdriver.FirefoxProfile()
# firefox_profile.set_preference('permissions.default.image', 2)
# firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
# browser = webdriver.Firefox(executable_path="E:\\geckodriver.exe",firefox_profile=firefox_profile)
#
# browser.get("https://www.taobao.com")

# phantomjs ，无界面的浏览器，多进程下phantomjs性能下降严重

#

#webdriver.phantomjs("https://detail.tmall.com/item.htm?spm=a1z10.1-b-s.w15914280-18716446969.2.277c5f3b15eIm1&id=570133905140&scene=taobao_shop&sku_properties=10004:1617715035;5919063:6536025")
browser = webdriver.PhantomJS(executable_path="E:/phantomjs-2.1.1-windows/bin/phantomjs.exe")
browser.get("https://detail.tmall.com/item.htm?spm=a1z10.1-b-s.w15914280-18716446969.2.277c5f3b15eIm1&id=570133905140&scene=taobao_shop&sku_properties=10004:1617715035;5919063:6536025")

print(browser.page_source)
browser.quit()